#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `prsync` package."""

from unittest.mock import MagicMock, patch

from click.testing import CliRunner

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

class TestPrsyncCli:
    @patch('prsync.cli.Prsync')
    def test_command_basic(self, m_Prsync):
        src = MagicMock()
        dst = MagicMock()
        prsync = m_Prsync.return_value
        runner = CliRunner()
        result = runner.invoke(cli.main, [src, dst])
        assert 'src = {0} dst = {1}'.format(src, dst) in result.output
        assert result.exit_code == 0

        m_Prsync.assert_called_with(src=src, dst=dst)
        prsync.run.assert_called_with()
