#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cached_venv` package."""


import unittest
from click.testing import CliRunner

from cached_venv import cli


class TestCached_venv(unittest.TestCase):
    """Tests for `cached_venv` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
