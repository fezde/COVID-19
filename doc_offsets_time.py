import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tools
import logging
import sys
import matplotlib.ticker as mtick
from population_database import population

def build_timeseries(df_base):
    df_base.set_index(["Province/State", "Country/Region"])
    df_base.drop(["Lat", "Long"], inplace=True, axis=1)
    df_base = df_base.groupby(['Country/Region']).sum()
    df_base = df_base.transpose()
    return df_base

# Load data from CSV
df_confirmed = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')  
df_deaths = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')  
df_recovered = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')  

df_confirmed = build_timeseries(df_confirmed)
df_deaths = build_timeseries(df_deaths)
df_recovered = build_timeseries(df_recovered)

cols = 4
rows = 4

fig, axes = plt.subplots(
    nrows=rows, 
    ncols=cols,
    figsize=(25,10) 
)
fig.suptitle("Correlation between confirmed and recovered cases for different time offsets", fontsize=16)


country = "China"

confirmed = df_confirmed[country].to_list()
deaths = df_deaths[country].to_list()
recovered = df_recovered[country].to_list()
logging.debug("%d - %d - %d" % (len(confirmed), len(deaths), len(recovered)))

step_size = 3

for row in range(rows):
    for col in range(cols):
        offset = (col * step_size) + (row * step_size * cols)


        tmp_deaths = deaths[offset : ]
        tmp_recovered = recovered[offset : ]

        if offset > 0:
            tmp_confirmed = confirmed[ : -1 * offset]
        else:
            tmp_confirmed = confirmed
        logging.debug("%d - %d - %d" % (len(tmp_confirmed), len(tmp_deaths), len(tmp_recovered)))

        df = pd.DataFrame(data={
            "confirmed": tmp_confirmed,
            # "deaths": tmp_deaths,
            "recovered": tmp_recovered,
        })

        corr = df.corr(method="pearson")
        corr_recovered = corr.at["confirmed", "recovered"]

        ax = df.plot(
            title = "Offset: %dd (r=%f)" % (offset, corr_recovered),
            lw=3,
            ax = axes[row, col]
        )
        ax.set_xlim(0, 70)
        ax.set_ylim(0, 85000    )



fig.tight_layout(pad = 3.0)
tools.save_chart_doc(fig, "page_correlations_fig3_time")
