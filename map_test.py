import os

import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import tools
import logging

# from helpers import slug

datafile = os.path.expanduser(
    '~/data/worldbank/API_IT.NET.USER.ZS_DS2_en_csv_v2.csv')
shapefile = 'geo_data/ne_10m_admin_0_countries.shp'

colors = 20
cmap = 'Reds'
figsize = (16, 10)
year = '2016'
cols = ['Country Name', 'Country Code', year]
title = 'Individuals using the Internet (% of population) in {}'.format(year)
imgfile = 'img_map.png'
description = "FEZ was here"

def rename_country(df, country_from, country_to):
    tmp = df[df["NAME_EN"] == country_from]
    logging.debug(tmp)
    index = tmp.index
    logging.debug(index)
    df.at[index,"NAME_EN"] = country_to
    return df


#gdf = gpd.read_file(shapefile)[['ADM0_A3', 'geometry']].to_crs('+proj=robin')
gdf = gpd.read_file(shapefile)[['NAME_EN', 'geometry']].to_crs('+proj=robin')

for n in gdf["NAME_EN"]:
    logging.debug(n)

gdf = rename_country(gdf, "United States of America", "US")
gdf = rename_country(gdf, "People's Republic of China", "China")

logging.debug(gdf[gdf["NAME_EN"] == "US"])
logging.debug(gdf[gdf["NAME_EN"] == "China"])