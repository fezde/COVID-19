import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tools
import logging
import sys
import random
import matplotlib.ticker as mtick
from population_database import population



def chart_top_ten(df, title, row, col, as_percent = False):
    topTen = df.max().sort_values(ascending=False).head(10).index.tolist()
    df = df.filter(items=topTen)

    ax = df.plot(
        ax=axes[row, col],
        title=title, 
        color = tools.get_chart_colors(df),
        legend = True,
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

fig, axes = plt.subplots(
        nrows=2, 
        ncols=3,
        figsize=(25,10) 
    )
fig.suptitle("Ill People", fontsize=16)

df_confirmed = tools.get_timeline("Confirmed") 
df_deaths = tools.get_timeline("Deaths") 
df_recovered = tools.get_timeline("Recovered") 

df_ill = df_confirmed - df_deaths - df_recovered

chart_top_ten(df_confirmed, "Confirmed (C)", 0, 0)
chart_top_ten(df_deaths, "Deaths (D)", 0, 1)

chart_top_ten(df_ill, "Ill People (IP)", 0, 2)



df_ill_relative = calculate_rate(df_confirmed - df_deaths - df_recovered)
chart_top_ten(df_ill_relative, "Ill People Rate (IPR)", 1, 2, as_percent=True)

df_confirmed_relative = calculate_rate(df_confirmed)
chart_top_ten(df_confirmed_relative, "Infection Rate (IR)", 1, 0, as_percent=True)

df_deaths_relative = calculate_rate(df_deaths)
chart_top_ten(df_deaths_relative, "Mortality Rate (MR)", 1, 1, as_percent=True)




tools.save_chart(fig, "ill")