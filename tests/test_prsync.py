#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `Prsync` class."""

from unittest.mock import MagicMock, patch

import pytest

from prsync import prsync
from prsync import cli

class TestPrsync:
    @patch('prsync.prsync.Prsync.init_source')
    @patch('prsync.prsync.Prsync.init_destination')
    def test_prsync_class(self, m_init_destination, m_init_source):
        from prsync import Prsync
        src = MagicMock()
        dst = MagicMock()
        prsync = Prsync(src=src, dst=dst)
        m_init_source.assert_called_with(src)
        m_init_destination.assert_called_with(dst)
