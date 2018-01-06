# -*- coding: utf-8 -*-


"""Main module."""


from prsync.prsource import PrSource
from prsync.prdestination import PrDestination


class PrSync:
    def __init__(self, src: str, dst: str) -> None:
        self.init_source(src)
        self.init_destination(dst)

    def run(self) -> None:
        self.source.validate()

    def init_source(self, source: str) -> None:
        self.source = PrSource(source)

    def init_destination(self, destination: str) -> None:
        self.destination = PrDestination(destination)
