from prsync.prfile import PrFile


class PrSource(PrFile):

    @property
    def source(self) -> str:
        return self.path
