# -*- coding: utf-8 -*-

"""Main module."""

import os.path

class Prsync:
    source = None

    def __init__(self, src, dst):
        self.init_source(src)
        self.init_destination(dst)

    def run(self):
        self.validate_source()

    def init_source(self, source):
        self.source = source

    def init_destination(self, destination):
        pass

    def validate_source(self):
        os.path.exists(self.source)
