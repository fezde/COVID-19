import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tools
import logging
import sys

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

correlations_deaths = []
correlations_recovered = []
counts = []

for country in df_confirmed.columns:
    offset = 0
    
    corr_min = 99
    corr_max = 0
    corr_deaths_max = 0
    corr_deaths_max_pos = 0
    corr_recovered_max = 0
    corr_recovered_max_pos = 0

    confirmed = df_confirmed[country].to_list()
    deaths = df_deaths[country].to_list()
    recovered = df_recovered[country].to_list()
    # cut all data with less then 50 confirmed cases
    while len(confirmed)>1 and confirmed[0] < 50:
        confirmed = confirmed[1:]
        deaths = deaths[1:]
        recovered = recovered[1:]

    
    while len(confirmed) > 10: # keep at least 10 days for comparison

        df = pd.DataFrame(data={
            "confirmed": confirmed,
            "deaths": deaths,
            "recovered": recovered
        })
        df.reindex()
        corr = df.corr(method="pearson")
        corr_deaths = corr.at["confirmed", "deaths"]
        corr_recovered = corr.at["confirmed", "recovered"]

        if corr_deaths > corr_deaths_max:
            corr_deaths_max = corr_deaths
            corr_deaths_max_pos = offset
        if corr_recovered > corr_recovered_max:
            corr_recovered_max = corr_recovered
            corr_recovered_max_pos = offset

        if corr_deaths > corr_max:
            corr_max = corr_deaths
        if corr_recovered > corr_max:
            corr_max = corr_recovered

        if corr_deaths < corr_min:
            corr_min = corr_deaths
        if corr_recovered < corr_min:
            corr_min = corr_recovered


        deaths = deaths[1:]
        recovered = recovered[1:]
        confirmed = confirmed[:-1]
        offset += 1
    
    correlations_deaths.append(corr_deaths_max_pos)
    correlations_recovered.append(corr_recovered_max_pos)
    counts.append(1)

df = pd.DataFrame(
    index = df_confirmed.columns,
    data={
        "Offset Deaths": correlations_deaths,
        "Offset Recovered": correlations_recovered,
        "Number of Countries": counts
    }
)

df = df[df["Offset Deaths"] > 0]
df = df[df["Offset Recovered"] > 0]

df = df.groupby(['Offset Deaths', 'Offset Recovered'], as_index=False).sum()


fig, axes = plt.subplots(
    nrows=1, 
    ncols=2,
    figsize=(25,10) 
)
fig.suptitle("Offsets between 'Confirmed Cases' and 'Deaths' or 'Recovered Cases'")

ax = df.plot(
    kind = "scatter",
    lw=3,
    x = "Offset Deaths",
    y = "Offset Recovered",
    c = "Number of Countries",
    s = 100,
    colormap='viridis',
    ax = axes[0]
)
ax.set_xlabel("Offset Deaths")
ax.set_ylabel("Offset Recovered")

boxstyle = {
    "linewidth": 3,
}
ax2 = df.boxplot(
    column = ["Offset Deaths", "Offset Recovered"],
    ax = axes[1],
    boxprops = boxstyle,
    flierprops = boxstyle,
    medianprops = boxstyle,
    whiskerprops = boxstyle,
    capprops = boxstyle,
)
fig.tight_layout(pad = 3.0)

tools.save_chart(fig, "offsets")
# This image is also used in doc_offsets.md as doc_offsets_fig2_offsets
