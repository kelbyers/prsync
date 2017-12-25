# -*- coding: utf-8 -*-


"""Main module."""


from prsync import PrSource


class Prsync:
    source = None

    def __init__(self, src: str, dst: str) -> None:
        self.init_source(src)
        self.init_destination(dst)

    def run(self) -> None:
        self.source.validate()

    def init_source(self, source: str) -> None:
        self.source = PrSource(source)

    def init_destination(self, destination: str) -> None:
        pass
