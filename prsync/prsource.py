from pathlib import Path
from prsync.prfile import PrFile


class PrSource(PrFile):

    @property
    def source(self) -> Path:
        return self.path
