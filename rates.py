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
        "Recovered": "time_series_covid19_recovered_global.csv"
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
    # df_base.drop(["Cruise Ship"], inplace=True, axis=1)

    return df_base

logging.info("Running %s" % __file__)

idx = 1
fig, axes = plt.subplots(
        nrows=2, 
        ncols=3,
        figsize=(25,10) 
    )
fig.suptitle("Recovery and Mortality Rates", fontsize=16)

chart_titles = {
    "totals": {
        "Confirmed": "Confirmed (C)", 
        "Deaths": "Deaths (D)", 
        "Recovered": "Recovered (R)"
    },
    "rate": {
        "Confirmed": "", 
        "Deaths": "Case Fatality Rate (CFR)", 
        "Recovered": "Case Survival Rate (CSR)"
    }
}
chart_max = {
        "Confirmed": 100, 
        "Deaths": 25, 
        "Recovered": 100
    }

df_confirmed = get_timeline("Confirmed")
topTen = df_confirmed.max().sort_values(ascending=False).head(10).index.tolist()
df_confirmed_filtered = df_confirmed.filter(items=topTen)
df_confirmed_filtered.plot(
        ax=axes[0, 0],
        title=chart_titles["totals"]["Confirmed"], 
        color = tools.get_chart_colors(df_confirmed_filtered),
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
        title=chart_titles["rate"][subj], 
        color = tools.get_chart_colors(df_chart_total),
        lw=3)
    ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax2.set_ylim(0, chart_max[subj])

    df_base_filtered.plot(
        ax=axes[0, idx],
        title=chart_titles["totals"][subj], 
        color = tools.get_chart_colors(df_base_filtered),
        lw=3)

    idx += 1


tools.save_chart(fig, "rates")
#plt.show()

