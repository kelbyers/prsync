from unittest.mock import MagicMock, patch
import pytest


class TestPrFile:
    def test_class(self):
        from prsync import PrFile
        file_path = MagicMock()
        prfile = PrFile(file_path)
        assert prfile.path == file_path

    @patch('os.path.exists')
    def test_validate(self, m_exists):
        from prsync import PrFile
        file_path = MagicMock()
        prfile = PrFile(file_path)
        prfile.validate()
        m_exists.assert_called_with(file_path)
