#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `PrSync` class."""

from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture(params=['valid', 'invalid'])
def file_path(request):
    return request.param


@pytest.fixture
def prsync_setup():
    from prsync import PrSync
    src = MagicMock()
    dst = MagicMock()
    prsync = PrSync(src=src, dst=dst)
    return (prsync, src, dst)


class TestPrsync:
    @patch('prsync.prsync.PrSync.init_source')
    @patch('prsync.prsync.PrSync.init_destination')
    def test_class(self, m_init_destination, m_init_source):
        from prsync import PrSync
        src = MagicMock()
        dst = MagicMock()
        PrSync(src=src, dst=dst)
        m_init_source.assert_called_with(src)
        m_init_destination.assert_called_with(dst)

    @patch('prsync.prsync.PrSync.init_destination')
    @patch('prsync.prsync.PrSource', autospec=True)
    def test_init_source(self, m_PrSource, _):
        prsync, src, dst = prsync_setup()
        pr_source = m_PrSource.return_value
        assert prsync.source == pr_source
        m_PrSource.assert_called_with(src)

    @patch('prsync.prsync.PrSync.init_destination')
    @patch('prsync.prsync.PrSource')
    def test_run_validates_source(self, m_PrSource, _):
        prsync, src, dst = prsync_setup()
        pr_source = m_PrSource.return_value

        prsync.run()

        pr_source.validate.assert_called_with()

    @patch('prsync.prsync.PrDestination', autospec=True)
    @patch('prsync.prsync.PrSync.init_source')
    def test_init_destination(self, _, m_PrDestination):
        prsync, src, dst = prsync_setup()
        pr_dest = m_PrDestination.return_value
        assert prsync.destination == pr_dest
        m_PrDestination.assert_called_with(dst)
