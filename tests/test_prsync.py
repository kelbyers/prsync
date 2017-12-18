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
        Prsync(src=src, dst=dst)
        m_init_source.assert_called_with(src)
        m_init_destination.assert_called_with(dst)

    @patch('prsync.prsync.PrSource', autospec=True)
    def test_init_source(self, m_PrSource):
        prsync, src, dst = prsync_setup()
        pr_source = m_PrSource.return_value
        assert prsync.source == pr_source
        m_PrSource.assert_called_with(src)

    @patch('prsync.prsync.PrSource')
    def test_run_validates_source(self, m_PrSource):
        prsync, src, dst = prsync_setup()
        pr_source = m_PrSource.return_value

        prsync.run()

        pr_source.validate.assert_called_with()
