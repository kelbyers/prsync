""""""

import os.path

class PrFile:
    def __init__(self, path):
        self.path = path

    def validate(self):
        os.path.exists(self.path)
