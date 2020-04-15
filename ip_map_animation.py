import os
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import tools
import logging
import mapclassify as mc

def rename_country(df, country_from, country_to):
    tmp = df[df["NAME_EN"] == country_from]
    logging.debug(tmp)
    index = tmp.index
    logging.debug(index)
    df.at[index,"NAME_EN"] = country_to
    return df

logging.debug("Running %s" % __file__)

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
logging.debug("\n%s" % df_ill)


merged = gdf.merge(df_ill, left_on='NAME_EN', right_on='Country/Region')

for col in df_ill.columns:
    parts = col.split("/")
    m = "0"+parts[0] if len(parts[0]) == 1 else parts[0]
    d = "0"+parts[1] if len(parts[1]) == 1 else parts[1]
    y = "20"+parts[2] if len(parts[2]) == 2 else parts[2]
    file_name = "charts/ill_people_map/tmp/ip_map_%s-%s-%s.png" % (y,m,d)
    if os.path.isfile(file_name):
        logging.debug("Skipping %s as the according output was already created" % col)
        continue

    col_data_above_zero = merged[merged[col]>0]
    num_records = len(col_data_above_zero[col])
    # col_data_above_zero = col_data[col_data]
    # logging.debug("\n%s"%col_data_above_zero)
    # logging.debug(col_data_above_zero[col])
    # logging.debug(num_records)
    
    # logging.debug("\n%s" % mc.FisherJenks(col_data_above_zero, k=colors))
    if num_records < colors * 2:
        logging.debug("Skipping %s as it only has %d records instead of %d" % (col, num_records, colors))
        continue

    fig, axes = plt.subplots(
        nrows=1,
        ncols=1,
        figsize=(16, 9)
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

    ax.set_title(
        "Ill people (IP) as of %s" % col,
        # fontdict={'fontsize': 20}, 
        # loc='left'
    )
    # ax.annotate(description, xy=(0.1, 0.1), size=12, xycoords='figure fraction')

    ax.set_axis_off()
    ax.set_xlim([-1.5e7, 1.7e7])
    # ax.get_legend().set_bbox_to_anchor((.12, .4))
    ax.get_figure()

    tools.save_tmp_chart(fig, file_name)

