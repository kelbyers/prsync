#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Prsync` class."""

from unittest.mock import MagicMock, patch

import pytest

@pytest.fixture(params=['valid', 'invalid'])
def file_path(request):
    return request.param

@pytest.fixture
def prsync_setup():
    from prsync import Prsync
    src = MagicMock()
    dst = MagicMock()
    prsync = Prsync(src=src, dst=dst)
    return (prsync, src, dst)

class TestPrsync:
    @patch('prsync.prsync.Prsync.init_source')
    @patch('prsync.prsync.Prsync.init_destination')
    def test_class(self, m_init_destination, m_init_source):
        from prsync import Prsync
        src = MagicMock()
        dst = MagicMock()
        prsync = Prsync(src=src, dst=dst)
        m_init_source.assert_called_with(src)
        m_init_destination.assert_called_with(dst)

    @patch('os.path')
    def test_init_source(self, m_os_path, prsync_setup):
        prsync, src, dst = prsync_setup
        assert prsync.source == src

    @patch('prsync.Prsync.validate_source')
    def test_run_validates_source(self, m_validate_source, prsync_setup):
        prsync, src, dst = prsync_setup

        prsync.run()

        m_validate_source.assert_called_with()

    @patch('os.path.exists')
    def test_validate_source_valid(self, m_exists, prsync_setup):
        prsync, src, dst = prsync_setup

        prsync.validate_source()

        m_exists.assert_called_with(src)

    @patch('os.path.exists')
    def test_validate_source_invalid(self, m_exists, prsync_setup):
        from prsync import PrsyncSourceError
        prsync, src, dst = prsync_setup
        m_exists.return_value = False

        with pytest.raises(PrsyncSourceError):
            prsync.validate_source()
