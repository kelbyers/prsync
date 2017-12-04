#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `prsync` package."""

import pytest

from click.testing import CliRunner

from prsync import prsync
from prsync import cli


# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'prsync.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output

class TestPrsync:
    def test_command_basic(self):
        src = 'a'
        dst = 'b'
        runner = CliRunner()
        result = runner.invoke(cli.main, [src, dst])
        assert result.output.strip() == 'src = {0} dst = {1}'.format(src, dst)
        assert result.exit_code == 0
