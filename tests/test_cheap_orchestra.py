#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cheap_orchestra` package."""

from cheap_orchestra import Maestro
from click.testing import CliRunner
from cheap_orchestra import cli
from unittest import TestCase


class TestCheapOrchestra(TestCase):
    """Tests for `cheap_orchestra` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.maestro = Maestro("tests/docker-compose.yml")

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_append_service_name_with_front_and_suffix_a_must_create_front_suffix_a_key(self):
        # given
        service_name = "front"
        suffix_name = "suffix-a"
        final_name = "front-suffix-a"
        # when
        compose_object = self.maestro.append_service_name(service_name, suffix_name)
        # then
        self.assertIsNotNone(compose_object["services"].get(final_name))

    def test_append_service_name_with_front_and_suffix_a_must_delete_front_key(self):
        # given
        service_name = "front"
        suffix_name = "suffix-a"
        # when
        compose_object = self.maestro.append_service_name(service_name, suffix_name)
        # then
        self.assertIsNone(compose_object["services"].get(service_name))

    def test_append_service_name_with_api_and_hiffen_suffix_b_must_create_api_suffix_b_key(self):
        # given
        service_name = "api"
        suffix_name = "-suffix_b"
        final_name = "api-suffix-b"
        # when
        compose_object = self.maestro.append_service_name(service_name, suffix_name)
        # then
        self.assertIsNotNone(compose_object["services"].get(final_name))

    def test_append_service_name_with_database_and_slash_suffix_c_must_create_database_suffix_c_key(self):
        # given
        service_name = "database"
        suffix_name = "/suffix_c"
        final_name = "database-suffix-c"
        # when
        compose_object = self.maestro.append_service_name(service_name, suffix_name)
        # then
        self.assertIsNotNone(compose_object["services"].get(final_name))

    def test_append_service_name_with_database_and_backslash_suffix_c_must_create_database_suffix_c_key(self):
        # given
        service_name = "database"
        suffix_name = "\suffix_c"
        final_name = "database-suffix-c"
        # when
        compose_object = self.maestro.append_service_name(service_name, suffix_name)
        # then
        self.assertIsNotNone(compose_object["services"].get(final_name))

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'cheap_orchestra.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
