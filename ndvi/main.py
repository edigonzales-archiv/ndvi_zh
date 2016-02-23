# -*- coding: utf-8 -*-
import os
import sys
import logging

from options import Options

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

def main():
    # Read the options and arguments from the command line (w/ some default settings).
    options = Options()
    opts = options.parse(sys.argv[1:])

    # Configure logging.
    FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename = opts.logfile, filemode = "w", format = FORMAT, level = logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())

    # Init QGIS
    app = QApplication(sys.argv)
    QgsApplication.setPrefixPath("/usr/local/qgis_master", True)
    QgsApplication.initQgis()
    QgsApplication.showSettings()

    #Load CIR orthofoto
    fileName = "/home/stefan/Downloads/1091-231.tif"
    fileInfo = QFileInfo(fileName)
    baseName = fileInfo.baseName()
    rlayer = QgsRasterLayer(fileName, baseName)
    if not rlayer.isValid():
        print "Layer failed to load!"

    print "************"
    print rlayer.width()
    print rlayer.bandCount()
    print rlayer.metadata()
    print rlayer.rasterType()
    print rlayer.dataProvider().colorTable(1)
    print "************"

    entries = []
    # Define band1
    boh1 = QgsRasterCalculatorEntry()
    boh1.ref = 'boh@1'
    boh1.raster = rlayer
    boh1.bandNumber = 1
    entries.append( boh1 )




if __name__ == '__main__':
    sys.exit(main())

# Exit QGIS
QgsApplication.exitQgis()
