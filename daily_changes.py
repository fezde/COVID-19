import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tools
import logging
import sys
import random
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



fig, axes = plt.subplots(
        nrows=2, 
        ncols=3,
        figsize=(25,10) 
    )
fig.suptitle("Growth rates", fontsize=16)

chart_titles = {
    "totals": {
        "Confirmed": "Confirmed (C)", 
        "Deaths": "Deaths (D)", 
        "Recovered": "Recovered (R)"
    },
    "newcases": {
        "Confirmed": "New C per day (rolling mean 7 days) - NCPD", 
        "Deaths": "New D per day (rolling mean 7 days) - NDPD", 
        "Recovered": ""
    },
    "growth": {
        "Confirmed": "Day to day growth of NCPD", 
        "Deaths": "Day to day growth of NDPD", 
        "Recovered": ""
    }
}

idx = 0


for subj in ["Confirmed", "Deaths"]:
    df_base = get_timeline(subj) 

    

    # get top ten only
    topTen = df_base.max().sort_values(ascending=False).head(10).index.tolist()
    df_chart_total = df_base.filter(items=topTen)  
    
    ax1 = df_chart_total.plot(
        ax=axes[idx, 0],
        title=chart_titles["totals"][subj], 
        color = tools.get_chart_colors(df_chart_total),
        legend = True,
        lw=3)



    df_diff = df_chart_total.diff()
    df_diff_mean = df_diff.rolling(window=7).mean()
    
    ax2 = df_diff_mean.plot(
        ax=axes[idx, 1],
        title=chart_titles["newcases"][subj], 
        color = tools.get_chart_colors(df_diff_mean),
        legend = False,
        lw=3)




    for i in range(10):
        df_chart_total.replace(i, np.nan, inplace=True)
    df_diff_mean_change= df_diff_mean.diff()
   
    ax2 = df_diff_mean_change.plot(
        ax=axes[idx, 2],
        title=chart_titles["growth"][subj], 
        color = tools.get_chart_colors(df_diff_mean_change),
        legend=False,
        lw=3)


    idx += 1

tools.save_chart(fig, "daily_changes")