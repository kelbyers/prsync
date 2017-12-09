#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Prsync` class."""

from unittest.mock import MagicMock, patch

import pytest

from prsync import prsync
from prsync import cli

@pytest.fixture(params=['valid', 'invalid'])
def file_path(request):
    return request.param

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
    def test_init_source(self, m_os_path):
        from prsync import Prsync
        src = MagicMock()
        dst = MagicMock()

        prsync = Prsync(src=src, dst=dst)
        assert prsync.source == src

    @patch('prsync.Prsync.validate_source')
    def test_run_validates_source(self, m_validate_source):
        from prsync import Prsync
        src = MagicMock()
        dst = MagicMock()
        prsync = Prsync(src=src, dst=dst)

        prsync.run()

        m_validate_source.assert_called_with()

    @patch('os.path.exists')
    def test_validate_source_valid(self, m_exists):
        from prsync import Prsync
        src = MagicMock()
        dst = MagicMock()
        prsync = Prsync(src=src, dst=dst)

        prsync.validate_source()

        m_exists.assert_called_with(src)
