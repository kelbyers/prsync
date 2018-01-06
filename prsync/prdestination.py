from pathlib import Path
from prsync.prfile import PrFile


class PrDestination(PrFile):
    def resolve(self) -> Path:
        try:
            return self.path.resolve()
        except FileNotFoundError:
            parent = self.path.parent.resolve()
            return parent / self.path.name
