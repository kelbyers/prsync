import os.path
from prsync import PrsyncSourceError, PrFile


class PrSource(PrFile):

    @property
    def source(self):
        return self.path

    # def validate(self):
    #     if not os.path.exists(self.source):
    #         raise PrsyncSourceError()
