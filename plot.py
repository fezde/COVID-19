import pandas as pd
import matplotlib.pyplot as plt

# Source: Google
population = {
    "China": 1.386 * 1000000000,
    "France": 66.99 * 1000000,
    "Germany": 82.79 * 1000000,
    "Iran": 81.16 * 1000000,
    "Italy": 60.48 * 1000000,
    "Spain": 46.66 * 1000000,
    "US": 327.2 * 1000000,
    "Netherlands": 17.18 * 1000000,
    "United Kingdom": 66.44 * 1000000,
    "Japan": 126.8 * 1000000,
    "Korea, South": 51.47 * 1000000,
    "Singapore": 5.612 * 1000000,
}

thresholds = {
    "Confirmed": 10000, 
    "Deaths": 100, 
    "Recovered": 100
}
idx = 0
fig, axes = plt.subplots(nrows=2, ncols=3)

for subj in ["Confirmed", "Deaths", "Recovered"]:
    print("Analysing %s" % subj)

    df_confirmed = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-%s.csv' % subj)  
    df_confirmed.set_index(["Province/State", "Country/Region"])
    df_confirmed.drop(["Lat", "Long"], inplace=True, axis=1)

    df_confirmed = df_confirmed.groupby(['Country/Region']).sum()
    

    df_confirmed = df_confirmed.transpose()

    df_confirmed.drop(["Cruise Ship"], inplace=True, axis=1)

    df_confirmed = df_confirmed[df_confirmed.columns[df_confirmed.max() > thresholds[subj]]]

    df_confirmed.plot(
        ax=axes[0,idx],
        title="%s Total" % subj, 
        lw=3)


    for col in df_confirmed.columns:
        if(not col in population.keys()):
            print("Missing popultion number for '%s'" % col)
            df_confirmed.drop(col, inplace=True, axis=1)
            break
        df_confirmed[col] /= population[col]
        df_confirmed[col] *= 100
  

    df_confirmed.plot(
        ax=axes[1,idx],
        title="%s in %% of population" % subj, 
        lw=3)

    idx += 1
plt.show()

