""""""

import os.path
from prsync import PrsyncSourceError

class PrFile:
    path = None

    def __init__(self, path):
        self.path = path

    def validate(self):
        if not os.path.exists(self.path):
            raise PrsyncSourceError(
                'Path does not exist: {0}'.format(self.path))
