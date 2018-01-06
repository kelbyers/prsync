from unittest.mock import MagicMock, patch
import pytest


@pytest.fixture
@patch('prsync.prfile.Path')
def prdst_class_setup(m_Path):
    from prsync import PrDestination
    dst_path = MagicMock()
    prdst = PrDestination(dst_path)
    return (prdst, dst_path)


class TestPrDestination:
    def test_class(self):
        from prsync import PrDestination
        from prsync import PrFile
        dst = '/a/path/to/something'

        prdst = PrDestination(dst)
        assert isinstance(prdst, PrFile)

    @patch('prsync.prfile.Path')
    def test_validate(self, m_Path, prdst_class_setup):
        prdst, dst_path = prdst_class_setup
        p_path = prdst.path
        r_path = p_path.resolve.return_value
        prdst.validate()
        assert prdst.path == p_path.resolve.return_value
        assert prdst.stats == r_path.stat.return_value

    @patch('prsync.prdestination.Path')
    def test_validate_not_exist(self, m_Path, prdst_class_setup):
        prdst, dst_path = prdst_class_setup
        p_path = prdst.path
        p_parent = p_path.parent
        p_path.resolve.side_effect = FileNotFoundError
        r_parent = p_parent.resolve.return_value
        r_path = r_parent / p_path.name

        prdst.validate()
        assert prdst.path == r_path
        assert prdst.stats == r_path.stat.return_value

    def test_validate_parent_not_exist(self, prdst_class_setup):
        prdst, dst_path = prdst_class_setup
        p_path = prdst.path
        p_parent = p_path.parent
        p_path.resolve.side_effect = FileNotFoundError
        p_parent.resolve.side_effect = FileNotFoundError

        with pytest.raises(FileNotFoundError):
            prdst.validate()
