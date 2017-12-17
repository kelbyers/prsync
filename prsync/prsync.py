# -*- coding: utf-8 -*-


"""Main module."""


from prsync import PrSource


class Prsync:
    source = None

    def __init__(self, src, dst):
        self.init_source(src)
        self.init_destination(dst)

    def run(self):
        self.source.validate()

    def init_source(self, source):
        self.source = PrSource(source)

    def init_destination(self, destination):
        pass
