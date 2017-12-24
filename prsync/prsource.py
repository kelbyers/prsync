from prsync import PrFile


class PrSource(PrFile):

    @property
    def source(self):
        return self.path
