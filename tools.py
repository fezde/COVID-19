import logging
import sys
from os import path, mkdir, getenv
from datetime import datetime
import matplotlib as plt
import matplotlib.font_manager as font_manager
from shutil import copyfile
from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import  PngInfo
import math
from population_database import population
import colorsys
import matplotlib.colors as mc
import pandas as pd


FORMAT = '%(asctime)-15s [%(levelname)7s] - %(name)s - %(message)s'
logging.basicConfig(stream=sys.stdout, format=FORMAT)

DEBUG_LEVEL = getenv('DEBUG_LEVEL') if getenv('DEBUG_LEVEL') else "DEBUG"
logging.getLogger().setLevel(DEBUG_LEVEL)
logging.getLogger('matplotlib.font_manager').setLevel(logging.INFO)
logging.getLogger('matplotlib.ticker').setLevel(logging.INFO)
logging.getLogger('matplotlib.colorbar').setLevel(logging.INFO)
logging.getLogger('numba.byteflow').setLevel(logging.INFO)
logging.getLogger('numba.interpreter').setLevel(logging.INFO)

fh = logging.FileHandler('warnings.log')
fh.setLevel(logging.WARNING)
logging.getLogger('').addHandler(fh)

logging.debug("matplotlibrc is used from '%s'" % (plt.matplotlib_fname()))

def save_tmp_chart(fig, fileName):
    
    fig.savefig(
        fileName, 
        bbox_inches='tight'
    )

    # fnt = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', 15)
    fnt = ImageFont.truetype('assets/Marvel-Regular.ttf', 15)
    
    img_orig = Image.open(fileName)
    img_new = Image.new('RGB', (img_orig.width, img_orig.height + 52), color = (255, 255, 255))
    img_new.paste(img_orig)

    
    d = ImageDraw.Draw(img_new)
    creation_time_text = "Created: " + datetime.now().strftime("%d %b %Y %H:%M:%S CET")
    copyright_text = "Copyright 2020 by Felix Kratzer (https://fezde.github.io/COVID-19) - Data Copyright by Johns Hopkins University (https://github.com/CSSEGISandData/COVID-19)"
    metadata = PngInfo()
    metadata.add_text("Copyright", copyright_text)
    metadata.add_text("Author", "Felix Kratzer (https://github.com/fezde)")

    text_width, text_height = d.textsize(creation_time_text, font=fnt)
    d.text((img_orig.width - (text_width + 5), img_orig.height), creation_time_text, font=fnt, fill=(0, 0, 0))

    text_width, text_height = d.textsize(copyright_text, font=fnt)
    d.text((img_orig.width - (text_width + 5), img_orig.height + 26), copyright_text, font=fnt, fill=(0, 0, 0))

    img_new.save(fileName, pnginfo=metadata)

    return (img_new, metadata)

def save_chart_doc(fig, filename):
    extension = "png"
    basePath = "docs-input/%s.%s" % (filename, extension)

    tempName = "temp." + extension
    save_tmp_chart(fig, tempName)
    copyfile(tempName, basePath)


def save_chart(fig, name):
    extension = "png"
    basePath = "charts/%s" % name
    webPath = "charts/_current"

    if not path.isdir(basePath):
        logging.info("Creating path for chart: %s" % basePath)
        mkdir(basePath)
    if not path.isdir(webPath):
        logging.info("Creating path for chart: %s" % webPath)
        mkdir(webPath)
    
    fileName = "%s/%s-%s.%s" % (basePath, name, datetime.now().strftime("%Y%m%d-%H%M%S"), extension)
    
    webName = "%s/%s.%s" % (webPath, name, extension)
    fileNameSmall = "%s/%s_small.%s" % (webPath, name, extension)
    logging.debug("Saving chart to: '%s' and '%s" % (fileName, webName))

    tempName = "temp." + extension
    (img_new, metadata) = save_tmp_chart(fig, tempName)

    

    img_small = img_new.resize((math.floor(img_new.width * 0.4), math.floor(img_new.height * 0.4)), Image.ANTIALIAS)
    img_small.save(fileNameSmall, pnginfo=metadata)

    copyfile(tempName, fileName)
    copyfile(tempName, webName)

# ####################################################################################
# Source Loading
# ####################################################################################
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

# ####################################################################################
# Color management
# ####################################################################################
def lighten_color(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)

    Source: https://stackoverflow.com/questions/37765197/darken-or-lighten-a-color-in-matplotlib
    """
    
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    r = colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
    r = list(r)
    
    for i in range(3):
        while r[i] < 0:
            r[i] = 1 - r[i]
        while r[i] > 1:
            r[i] = r[i] -1
    return (r[0], r[1], r[2]) #colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])



def get_chart_colors(data_frame):
    return [colorcycle[list(population.keys()).index(country)] for country in data_frame.columns]

def get_chart_styles(data_frame):
    return [stylecycle[list(population.keys()).index(country)] for country in data_frame.columns]


#colorcycle = ['#163028', '#244c44', '#326a63', '#408985', '#4eaaab', '#5cccd4', '#6deeff', '#4bcbf4', '#46a8e2', '#5483c7', '#635ea4', '#683878', '#610b49']
colorcycle = ['#005e8aff', '#4764a4ff', '#8364b0ff', '#bc5eaaff', '#eb5a93ff', '#ff6470ff', '#ff8145ff', '#ffa600ff']
# colorcycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
orig_colorcycle = colorcycle.copy()
logging.debug("Color cycle: %s" % colorcycle)

basestyles = ["#fe2fe2x-", "b.-", "bo-", "b1-", "b|-", "b2-"]
stylecycle = []
for i in range(len(basestyles)):
    for _ in range(len(colorcycle)):
        stylecycle.append(basestyles[i])
logging.debug("Style cycle: %s" % stylecycle)

count = 0
step_size = 0.2
while len(population) > len(colorcycle):
    count += 1
    logging.debug("Enlarging color cycle")
    for c in orig_colorcycle:
        # c2 = lighten_color(c, 1.0-(count * step_size))
        # colorcycle.append(c2)
        c2 = lighten_color(c, 1.0+(count * step_size))
        colorcycle.append(c2)
        # colorcycle.append(c)
# random.shuffle(colorcycle)

tmpcc = colorcycle.copy()
colorcycle = []
for c in tmpcc:
    newc = plt.colors.to_rgba(c)
    logging.debug("%s -> %s" % (c,newc))
    colorcycle.append(newc)

# specify the custom font to use
font_dirs = ['assets', ]
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
font_list = font_manager.createFontList(font_files)
font_manager.fontManager.ttflist.extend(font_list)

plt.rcParams['font.family'] = 'Marvel'