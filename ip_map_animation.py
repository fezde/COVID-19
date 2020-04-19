import os
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import tools
import logging
import mapclassify as mc
from datetime import datetime


def rename_country(df, country_from, country_to):
    tmp = df[df["NAME_EN"] == country_from]
    logging.debug(tmp)
    index = tmp.index
    logging.debug(index)
    df.at[index, "NAME_EN"] = country_to
    return df


logging.info("Running %s" % __file__)

shapefile = 'geo_data/ne_10m_admin_0_countries.shp'

colors = 20
cmap = 'Reds'
figsize = (16, 10)


#gdf = gpd.read_file(shapefile)[['ADM0_A3', 'geometry']].to_crs('+proj=robin')
gdf = gpd.read_file(shapefile)[['NAME_EN', 'geometry']].to_crs('+proj=robin')

# Rename Countries
gdf = rename_country(gdf, "United States of America", "US")
gdf = rename_country(gdf, "People's Republic of China", "China")

df_confirmed = tools.get_timeline("Confirmed")
df_deaths = tools.get_timeline("Deaths")
df_recovered = tools.get_timeline("Recovered")

df_ill = df_confirmed - df_deaths - df_recovered

df_ill = df_ill.transpose()


merged = gdf.merge(df_ill, left_on='NAME_EN', right_on='Country/Region')

if not os.path.isdir("charts/ill_people_map"):
    os.mkdir("charts/ill_people_map")
if not os.path.isdir("charts/ill_people_map/tmp"):
    os.mkdir("charts/ill_people_map/tmp")


total_per_day = {}

for col in df_ill.columns:
    total_per_day[col] = merged[col].sum()

    parts = col.split("/")
    m = "0"+parts[0] if len(parts[0]) == 1 else parts[0]
    d = "0"+parts[1] if len(parts[1]) == 1 else parts[1]
    y = "20"+parts[2] if len(parts[2]) == 2 else parts[2]
    file_name = "charts/ill_people_map/tmp/ip_map_%s-%s-%s.png" % (y, m, d)
    if os.path.isfile(file_name):
        logging.debug(
            "Skipping %s as the according output was already created" % col)
        continue

    col_data_above_zero = merged[merged[col] > 0]
    num_records = len(col_data_above_zero[col])

    if num_records < colors * 2:
        logging.debug("Skipping %s as it only has %d records instead of %d" % (
            col, num_records, colors))
        continue

    fig = plt.figure(figsize=(16, 9))
    axes = fig.add_subplot(111)
    axes2 = fig.add_subplot(
        111,
        autoscale_on=True,
        alpha=0.5,
        facecolor="None",
    )

    ax = merged.dropna().plot(
        column=col,
        ax=axes,
        cmap=cmap,
        # figsize=figsize,
        # scheme='equal_interval',
        scheme='fisher_jenks',
        # scheme='QUANTILES',
        k=colors,
        legend=True,
        lw=1,
    )

    merged[merged.isna().any(axis=1)].plot(ax=ax, color='#fafafa', hatch='///')
    ax.set_axis_off()
    ax.get_legend().set_bbox_to_anchor((.155, .56))
    ax.set_xlim([-1.5e7, 1.7e7])
    title_date = datetime.strptime(col, "%m/%d/%y").strftime("%d %b %Y")
    ax.set_title("Ill people (IP) as of %s" % title_date)

    df_total = pd.DataFrame.from_dict(total_per_day, orient='index')
    logging.debug("\n%s" % df_total)
    ax2 = df_total.plot(
        ax=axes2,
        legend=False,
        lw=3,
        color=(0.117, 0.449, 0.703, 0.5),
    )
    ax2.get_yaxis().set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    y = ax2.lines[0].get_ydata()[-1]
    x = ax2.lines[0].get_xdata()[-1]

    ax2.plot(
        x, y,
        marker='o',
        color=(0.117, 0.449, 0.703, 1),
    )
    ax2.annotate(
       f"Ill people worldwide: {y:,d}",
        xy=(x, y),
        xytext=(-6, 0),
        color=ax2.lines[0].get_color(),
        # xycoords=ax.get_yaxis_transform(),
        textcoords="offset points",
        size=14,
        va="center",
        ha="right",
    )

    fig.tight_layout()
    tools.save_tmp_chart(fig, file_name)
