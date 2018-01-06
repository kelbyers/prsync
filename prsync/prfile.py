""""""

import sys
from pathlib import Path

from prsync import os_imports


class PrFile:
    block_size = None
    path = None
    stats = None

    def __init__(self, path: str) -> None:
        self.path = Path(path)

    def setup(self) -> None:
        self.validate()
        self.get_block_size()

    def resolve(self) -> Path:
        return self.path.resolve()

    def validate(self) -> None:
        self.path = self.resolve()

    @property
    def stats(self) -> os_imports.stat_result:
        return self.path.stat()

    def get_block_size(self) -> None:
        if sys.platform == 'win32':
            conn = os_imports.wmi.WMI()
            volume = conn.Win32_Volume(Caption=self.path.parts[0])[0]
            self.block_size = volume.BlockSize
        else:
            self.block_size = os_imports.statvfs(self.path).f_bsize

    def __eq__(self, other):
        """Compare the size and timestamp of this PrFile to `other'.
        Return: boolean
        """

        if self.stats.st_size == other.stats.st_size:
            if self.stats.st_mtime_ns == other.stats.st_mtime_ns:
                return True

        return False
