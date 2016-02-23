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

    # Init qgis
    app = QApplication(sys.argv)
    QgsApplication.setPrefixPath("/usr/local/qgis_master", True)
    QgsApplication.initQgis()
    QgsApplication.showSettings()
    #qgs = QgsApplication(sys.argv, False)
    #qgs.initQgis()

    vlayer = QgsVectorLayer("/home/stefan/Downloads/2549/Liegenschaften__Liegenschaft.shp", "Liegenschaften__Liegenschaft", "ogr")
    if not vlayer.isValid():
        print "Layer failed to load!"

    print vlayer.extent().asPolygon()

    #Load CIR orthofoto
    fileName = "/home/stefan/Downloads/1091-231.tif"
    fileInfo = QFileInfo(fileName)
    baseName = fileInfo.baseName()
    rlayer = QgsRasterLayer(fileName, baseName)
    if not rlayer.isValid():
        print "Layer failed to load!"

    print "************"
    print rlayer.width()
    print "************"





if __name__ == '__main__':
    sys.exit(main())

QgsApplication.exitQgis()
