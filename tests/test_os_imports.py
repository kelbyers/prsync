import sys
from unittest.mock import patch
import pytest


@pytest.yield_fixture
def os_imports():
    from prsync import os_imports
    yield os_imports
    del os_imports
    try:
        del sys.modules['prsync.os_imports']
    except KeyError:
        pass


@patch('prsync.os_imports.wmi')
@patch('prsync.os_imports.system', return_value='Windows')
def test_windows(m_system, m_wmi, os_imports):
    assert os_imports.wmi == m_wmi


@patch('prsync.os_imports.statvfs')
@patch('prsync.os_imports.system', return_value='Non-Windows')
def test_non_windows(m_system, m_statvfs, os_imports):
    assert os_imports.statvfs == m_statvfs
