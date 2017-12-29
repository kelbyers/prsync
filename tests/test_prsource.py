""""""

from unittest.mock import MagicMock, patch
import pytest


@pytest.fixture
def pr_source_setup():
    from prsync import PrSource
    src = MagicMock()
    pr_source = PrSource(src)
    return (pr_source, src)


class TestPrSource:
    def test_class(self):
        from prsync import PrSource
        from prsync import PrFile

        source_file = '/a/file/path'
        prsource = PrSource(source_file)
        assert isinstance(prsource, PrFile)
