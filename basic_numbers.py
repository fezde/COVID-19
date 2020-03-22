import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tools
import logging
import sys
import matplotlib.ticker as mtick
from population_database import population


thresholds = {
    "Confirmed": 10000, 
    "Deaths": 100, 
    "Recovered": 100
}
idx = 0
fig, axes = plt.subplots(
        nrows=2, 
        ncols=3,
        figsize=(25,10) 
    )

for subj in ["Confirmed", "Deaths", "Recovered"]:
    logging.debug("Analysing %s" % subj)

    # Load data from CSV
    df_base = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-%s.csv' % subj)  
    df_base.set_index(["Province/State", "Country/Region"])
    df_base.drop(["Lat", "Long"], inplace=True, axis=1)

    # Group by Country
    df_base = df_base.groupby(['Country/Region']).sum()
    
    # Create a timeline
    df_base = df_base.transpose()
    
    # Drop "countries" that we will not handle
    df_base.drop(["Cruise Ship"], inplace=True, axis=1)

    # Create first chart
    df_chart_total = df_base
    # get top ten only
    topTen = df_chart_total.max().sort_values(ascending=False).head(10).index.tolist()
    topTwenty = df_chart_total.max().sort_values(ascending=False).head(20).index.tolist()
    df_chart_total = df_chart_total.filter(items=topTen)

    df_chart_total.plot(
        ax=axes[0,idx],
        title="%s Total" % subj, 
        lw=3)


    # Bring total numbers into relation to country's population
    df_chart_relative = df_base
    
    for col in df_chart_relative.columns:
        if col in topTwenty:
            #logging.debug("Recalculating values for: %s" % col)
            if(not col in population.keys()):
                logging.warning("Missing popultion number for '%s'" % col)
                df_chart_relative.drop(col, inplace=True, axis=1)
                continue
            df_chart_relative[col] /= population[col]
            df_chart_relative[col] *= 100
        else:
            df_chart_relative.drop(col, inplace=True, axis=1)

    
    # get top ten only
    topTen = df_chart_relative.max().sort_values(ascending=False).head(10).index.tolist()
    df_chart_relative = df_chart_relative.filter(items=topTen)
    
    


    
    ax2 = df_chart_relative.plot(
        ax=axes[1,idx],
        title="%s in %% of population" % subj, 
        lw=3)
    ax2.yaxis.set_major_formatter(mtick.PercentFormatter())

    idx += 1


tools.save_chart(fig, "basic_numbers")
#plt.show()

