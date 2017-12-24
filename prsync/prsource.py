import os.path
from prsync import PrsyncSourceError, PrFile


class PrSource(PrFile):
    source = None

    def __init__(self, source):
        self.source = source

    def validate(self):
        if not os.path.exists(self.source):
            raise PrsyncSourceError()
