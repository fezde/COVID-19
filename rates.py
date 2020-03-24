import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tools
import logging
import sys
import matplotlib.ticker as mtick
from population_database import population

def get_timeline(subj):
    filenames = {
        "Confirmed": "time_series_covid19_confirmed_global.csv", 
        "Deaths": "time_series_covid19_deaths_global.csv", 
        "Recovered": "time_series_19-covid-Recovered.csv"
    }

    # Load data from CSV
    df_base = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/' + filenames[subj])  
    df_base.set_index(["Province/State", "Country/Region"])
    df_base.drop(["Lat", "Long"], inplace=True, axis=1)

    # Group by Country
    df_base = df_base.groupby(['Country/Region']).sum()
    
    # Create a timeline
    df_base = df_base.transpose()
    
    # Drop "countries" that we will not handle
    df_base.drop(["Cruise Ship"], inplace=True, axis=1)

    return df_base

idx = 1
fig, axes = plt.subplots(
        nrows=2, 
        ncols=3,
        figsize=(25,10) 
    )
fig.suptitle("Recovery and Mortality Rates", fontsize=16)


df_confirmed = get_timeline("Confirmed")
topTen = df_confirmed.max().sort_values(ascending=False).head(10).index.tolist()
df_confirmed_filtered = df_confirmed.filter(items=topTen)
df_confirmed_filtered.plot(
        ax=axes[0, 0],
        title="Confirmed Total", 
        lw=3)

titles = {
    "Recovered": "Recovery Rate",
    "Deaths": "Mortality Rate"
}

axes[1,0].axis('off')

for subj in ["Deaths", "Recovered"]:
    logging.debug("Analysing %s" % subj)

    df_base = get_timeline(subj) 
    

    # Create first chart
    df_chart_total = (df_base / df_confirmed) * 100
    # get top ten only
    topTen = df_base.max().sort_values(ascending=False).head(10).index.tolist()
    

    df_chart_total = df_chart_total.filter(items=topTen)
    df_base_filtered = df_base.filter(items=topTen)

    ax2 = df_chart_total.plot(
        ax=axes[1, idx],
        title=titles[subj], 
        lw=3)
    ax2.yaxis.set_major_formatter(mtick.PercentFormatter())

    df_base_filtered.plot(
        ax=axes[0, idx],
        title="%s Total" % subj, 
        lw=3)

    idx += 1


tools.save_chart(fig, "rates")
#plt.show()

