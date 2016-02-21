# -*- coding: utf-8 -*-
import os
import sys
import logging

from options import Options

from PyQt4.QtCore import *
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




if __name__ == '__main__':
    sys.exit(main())
