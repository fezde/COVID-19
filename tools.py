import logging
import sys
from os import path, mkdir
from datetime import datetime
import matplotlib
from shutil import copyfile
from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import  PngInfo
import math


FORMAT = '%(asctime)-15s [%(levelname)7s] - %(name)s - %(message)s'
logging.basicConfig(stream=sys.stdout, format=FORMAT)

logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger('matplotlib.font_manager').setLevel(logging.INFO)
logging.getLogger('matplotlib.ticker').setLevel(logging.INFO)
logging.getLogger('matplotlib.colorbar').setLevel(logging.INFO)

logging.debug("matplotlibrc is used from '%s'" % (matplotlib.matplotlib_fname()))

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

    fig.savefig(
        fileName, 
        bbox_inches='tight'
    )

    
    fnt = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', 15)
    
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

    img_small = img_new.resize((math.floor(img_new.width * 0.4), math.floor(img_new.height * 0.4)), Image.ANTIALIAS)
    img_small.save(fileNameSmall, pnginfo=metadata)

    copyfile(fileName, webName)