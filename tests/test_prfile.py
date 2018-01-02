from unittest.mock import MagicMock, patch
import pytest


@pytest.fixture
@patch('prsync.prfile.Path')
def pr_file_setup(m_Path):
    from prsync import PrFile
    file_path = MagicMock()
    pr_file = PrFile(file_path)
    return (pr_file, file_path)


@pytest.fixture
@patch('prsync.prfile.Path')
def pr_source_setup(m_Path):
    from prsync import PrSource
    src = MagicMock()
    pr_source = PrSource(src)
    return (pr_source, src)


@pytest.fixture(params=['win32', '*nix'])
def platform(request):
    return request.param


def make_pr_file_class(klass):
    if klass == 'PrFile':
        return pr_file_setup()
    elif klass == 'PrSource':
        return pr_source_setup()


@pytest.fixture(params=['PrFile', 'PrSource'])
def pr_file_class_name(request):
    return request.param


@pytest.fixture
def pr_file_class_setup(pr_file_class_name):
    return make_pr_file_class(pr_file_class_name)


@pytest.fixture(params=[True, False])
def equals(request):
    return request.param


class TestPrFile:
    @patch('prsync.prfile.Path')
    def test_class(self, m_Path):
        from prsync import PrFile
        file_path = MagicMock()
        prfile = PrFile(file_path)
        m_Path.assert_called_with(file_path)
        assert prfile.path == m_Path.return_value

    @patch('prsync.prfile.PrFile.get_block_size')
    @patch('prsync.prfile.PrFile.validate')
    def test_setup(self, m_validate, m_get_block_size, pr_file_setup):
        prfile, file_path = pr_file_setup
        prfile.setup()

        m_validate.assert_called_with()
        m_get_block_size.assert_called_with()

    @patch('prsync.prfile.Path')
    @patch('prsync.prfile.os_imports')
    @patch('prsync.prfile.sys')
    def test_get_block_size(self, m_sys, m_os_imports, m_Path, platform):
        m_os_imports.NAME = m_sys.platform = platform

        from prsync import PrFile
        file_path = MagicMock()
        prfile = PrFile(file_path)

        prfile.get_block_size()

        path = m_Path.return_value
        if platform == 'win32':
            conn = m_os_imports.wmi.WMI.return_value
            volume = conn.Win32_Volume.return_value[0]
            conn.Win32_Volume.assert_called_with(Caption=path.parts[0])
            block_size = volume.BlockSize
        else:
            m_statvfs = m_os_imports.statvfs
            m_statvfs.assert_called_with(path)
            stats = m_statvfs.return_value
            block_size = stats.f_bsize

        assert prfile.block_size == block_size

    @patch('prsync.prfile.Path')
    def test_validate(self, m_Path, pr_file_class_setup):
        prfile, file_path = pr_file_class_setup
        p_path = m_Path.return_value
        r_path = p_path.resolve.return_value
        prfile.validate()
        assert prfile.path == p_path.resolve.return_value
        assert prfile.stats == r_path.stat.return_value

    @patch('prsync.prfile.Path')
    def test_validate_invalid(self, m_Path, pr_file_class_setup):
        from prsync import PrsyncSourceError
        pr_file, file_path = pr_file_class_setup
        path_path = m_Path.return_value
        path_path.resolve.side_effect = FileNotFoundError

        with pytest.raises(FileNotFoundError):
            pr_file.validate()

    @patch('prsync.prfile.Path')
    def test_compare_equals(self, m_Path, pr_file_class_name):
        first, _ = make_pr_file_class(pr_file_class_name)
        other, _ = make_pr_file_class(pr_file_class_name)
        first.stats = MagicMock()
        other.stats = first.stats

        eq = first == other

        assert eq

    @patch('prsync.prfile.Path')
    def test_compare_no_stats(self, m_Path, pr_file_class_name):
        first, _ = make_pr_file_class(pr_file_class_name)
        other, _ = make_pr_file_class(pr_file_class_name)
        first.stats = None

        with pytest.raises(AttributeError):
            eq = first == other

    @patch('prsync.prfile.Path')
    def test_compare_no_other_stats(self, m_Path, pr_file_class_name):
        first, _ = make_pr_file_class(pr_file_class_name)
        other, _ = make_pr_file_class(pr_file_class_name)
        first.stats = MagicMock()
        other.stats = None

        with pytest.raises(AttributeError):
            eq = first == other

    @patch('prsync.prfile.Path')
    def test_compare_sizes(self, m_Path, pr_file_class_name, equals):
        first, _ = make_pr_file_class(pr_file_class_name)
        other, _ = make_pr_file_class(pr_file_class_name)
        first.stats = MagicMock()
        other.stats = MagicMock()

        first.stats.st_size.__eq__.return_value = equals
        first.stats.st_mtime_ns.__eq__.return_value = True

        eq = first == other

        assert eq is equals
        first.stats.st_size.__eq__.assert_called_with(
            other.stats.st_size,
        )

    @patch('prsync.prfile.Path')
    def test_compare_times(self, m_Path, pr_file_class_name, equals):
        first, _ = make_pr_file_class(pr_file_class_name)
        other, _ = make_pr_file_class(pr_file_class_name)
        first.stats = MagicMock()
        other.stats = MagicMock()

        first.stats.st_size.__eq__.return_value = True
        first.stats.st_mtime_ns.__eq__.return_value = equals

        eq = first == other

        assert eq is equals
        first.stats.st_mtime_ns.__eq__.assert_called_with(
            other.stats.st_mtime_ns,
        )
