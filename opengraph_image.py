import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tools
import logging
import sys
import random
import matplotlib.ticker as mtick
from population_database import population

def chart_top_ten(df, title, axes, row=0, col=0, as_percent=False):
    topTen = df.max().sort_values(ascending=False).head(10).index.tolist()
    df = df.filter(items=topTen)
    can_we_do_subplots = isinstance(axes, np.ndarray)
    logging.debug("type(axes)=%s" % type(axes))
    logging.debug("Can we do subplots? %s" % can_we_do_subplots)
    if can_we_do_subplots:
        ax = df.plot(
            ax=axes[row, col],
            title=title,
            color=tools.get_chart_colors(df),
            legend=True,
            lw=3)
    else:
        ax = df.plot(
            title=title,
            ax=axes,
            color=tools.get_chart_colors(df),
            legend=True,
            lw=3)

    if as_percent:
        ax.yaxis.set_major_formatter(mtick.PercentFormatter())


def calculate_rate(df):
    topThirty = df.max().sort_values(ascending=False).head(30).index.tolist()
    df = df.filter(items=topThirty)

    for col in df.columns:
        #logging.debug("Recalculating values for: %s" % col)
        if(not col in population.keys()):
            logging.warning("Missing popultion number for '%s'" % col)
            df.drop(col, inplace=True, axis=1)
            continue
        df[col] /= population[col]
        df[col] *= 100
    return df

logging.info("Running %s" % __file__)

df_confirmed = tools.get_timeline("Confirmed")
df_deaths = tools.get_timeline("Deaths")
df_recovered = tools.get_timeline("Recovered")

df_ill = df_confirmed - df_deaths - df_recovered

df_ill_relative = calculate_rate(df_confirmed - df_deaths - df_recovered)



logging.info("Creating image for og:image from ill.py")
fig2, axes2 = plt.subplots(
    nrows=1,
    ncols=1,
    figsize=(10, 5)
)
chart_top_ten(df_ill_relative, "COVID-19 :: Ill People Rate (IPR)", axes2, as_percent=True)
tools.save_chart(fig2, "opengraph_image")