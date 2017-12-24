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

        source_file = MagicMock()
        prsource = PrSource(source_file)
        assert isinstance(prsource, PrFile)

    @patch('os.path')
    def test_validate(self, m_os_path, pr_source_setup):
        pr_source, src_file = pr_source_setup
        pr_source.validate()

        m_os_path.exists.assert_called_with(src_file)

    @patch('os.path')
    def test_validate_invalid(self, m_os_path, pr_source_setup):
        from prsync import PrsyncSourceError
        pr_source, src_file = pr_source_setup
        m_os_path.exists.return_value = False

        with pytest.raises(PrsyncSourceError):
            pr_source.validate()

        m_os_path.exists.assert_called_with(src_file)
