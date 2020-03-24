import logging
import sys
from os import path, mkdir
from datetime import datetime
import matplotlib
from shutil import copyfile

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
    webPath = "docs/charts"

    if not path.isdir(basePath):
        logging.info("Creating path for chart: %s" % basePath)
        mkdir(basePath)
    if not path.isdir(webPath):
        logging.info("Creating path for chart: %s" % webPath)
        mkdir(webPath)
    
    fileName = "%s/%s-%s.%s" % (basePath, name, datetime.now().strftime("%Y%m%d-%H%M%S"), extension)
    webName = "%s/%s.%s" % (webPath, name, extension)
    logging.debug("Saving chart to: '%s' and '%s" % (fileName, webName))

    fig.savefig(
        fileName, 
        bbox_inches='tight'
    )

    copyfile(fileName, webName)