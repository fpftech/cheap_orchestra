#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cheap_orchestra` package."""


import unittest
from click.testing import CliRunner

from cheap_orchestra import cheap_orchestra
from cheap_orchestra import cli


class TestCheap_orchestra(unittest.TestCase):
    """Tests for `cheap_orchestra` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'cheap_orchestra.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
