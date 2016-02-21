# -*- coding: utf-8 -*-
from argparse import ArgumentParser

class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/ndvi'
        self.parser = ArgumentParser(usage=usage)

        self.parser.add_argument('--log',
                                action = 'store',
                                type = str,
                                default = 'ndvi.log',
                                dest ='logfile',
                                help = 'Log message to given file. Default: ndvi.log.')

    def parse(self, args=None):
        return self.parser.parse_args(args)
