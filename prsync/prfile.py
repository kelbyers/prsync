""""""

import sys
from pathlib import Path

from prsync import os_imports


class PrFile:
    path = None
    block_size = None

    def __init__(self, path: str) -> None:
        self.path = Path(path)

    def setup(self) -> None:
        self.validate()
        self.get_block_size()

    def validate(self) -> None:
        self.path = Path(self.path).resolve()

    def get_block_size(self) -> None:
        if sys.platform == 'win32':
            conn = os_imports.wmi.WMI()
            volume = conn.Win32_Volume(Caption=self.path.parts[0])[0]
            self.block_size = volume.BlockSize
        else:
            self.block_size = os_imports.statvfs(self.path).f_bsize
