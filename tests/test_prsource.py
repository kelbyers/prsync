""""""

from unittest.mock import MagicMock, patch
import pytest

class TestPrSource:
    def test_class(self):
        from prsync import PrSource

        source_file = MagicMock()
        pr_source = PrSource(source_file)
