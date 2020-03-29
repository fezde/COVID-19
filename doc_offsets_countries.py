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

topCountries = df_confirmed.max().sort_values(ascending=False).head(10).index.tolist()
logging.debug("Countries to be analyzed: %s" % topCountries)

fig, axes = plt.subplots(
    nrows=2, 
    ncols=5,
    figsize=(25,10) 
)
fig.suptitle("Correlation to Confirmed cases", fontsize=16)
idx = 0

for country in topCountries:
    offset = 0
    correlations_deaths = []
    correlations_recovered = []

    
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
    while confirmed[0] < 50:
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

        correlations_deaths.append(corr_deaths)
        correlations_recovered.append(corr_recovered)
        # logging.debug("%s %d %s" % (country, offset, corr))
        # logging.debug("correlation confirmed deaths:    %f" % corr.at["confirmed", "deaths"])
        # logging.debug("correlation confirmed recovered: %f" % corr.at["confirmed", "recovered"])

        deaths = deaths[1:]
        recovered = recovered[1:]
        confirmed = confirmed[:-1]
        offset += 1

    df = pd.DataFrame(data={
        "deaths": correlations_deaths,
        "recovered": correlations_recovered
    })
    ax = df.plot(
        title = country,
        lw=3,
        ax = axes[int((idx - (idx % 5)) / 5), idx % 5]
    )
    ax.set_xlabel("Days offset")
    ax.set_ylabel("Correlation")


    annot_y_pos = corr_deaths_max - ((corr_deaths_max - corr_min) * 0.13)
    ax.annotate('offset = %d' % corr_deaths_max_pos, 
        xy=(corr_deaths_max_pos, corr_deaths_max), 
        xytext=(corr_deaths_max_pos, annot_y_pos),
        arrowprops={
            "facecolor": plt.rcParams['axes.prop_cycle'].by_key()['color'][0], 
            # "shrink": 0.6
            },
    )
    
    annot_y_pos = corr_recovered_max - ((corr_max - corr_min) * 0.13)
    ax.annotate(
        # 'offset = 12',
        'offset = %d' % corr_recovered_max_pos, 
        xy=(corr_recovered_max_pos, corr_recovered_max), 
        xytext=(corr_recovered_max_pos, annot_y_pos),
        arrowprops={
            "facecolor": plt.rcParams['axes.prop_cycle'].by_key()['color'][1], 
        },
    )

    idx += 1

fig.tight_layout(pad = 3.0)
tools.save_chart_doc(fig,"page_correlations_fig1_countries")
