from unittest.mock import MagicMock, patch
import pytest


@pytest.fixture
def pr_file_setup():
    from prsync import PrFile
    file_path = MagicMock()
    pr_file = PrFile(file_path)
    return (pr_file, file_path)


@pytest.fixture
def pr_source_setup():
    from prsync import PrSource
    src = MagicMock()
    pr_source = PrSource(src)
    return (pr_source, src)


@pytest.fixture(params=['PrFile', 'PrSource'])
def pr_file_class_setup(request):
    if request.param == 'PrFile':
        return pr_file_setup()
    elif request.param == 'PrSource':
        return pr_source_setup()


class TestPrFile:
    def test_class(self):
        from prsync import PrFile
        file_path = MagicMock()
        prfile = PrFile(file_path)
        assert prfile.path == file_path

    @patch('os.path.exists')
    def test_validate(self, m_exists, pr_file_class_setup):
        prfile, file_path = pr_file_class_setup
        prfile.validate()
        m_exists.assert_called_with(file_path)

    @patch('os.path')
    def test_validate_invalid(self, m_os_path, pr_file_class_setup):
        from prsync import PrsyncSourceError
        pr_file, file_path = pr_file_class_setup
        m_os_path.exists.return_value = False

        with pytest.raises(PrsyncSourceError):
            pr_file.validate()

        m_os_path.exists.assert_called_with(file_path)
