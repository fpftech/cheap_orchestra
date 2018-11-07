#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cheap_orchestra` package."""

from click.testing import CliRunner
from cheap_orchestra import cli
from unittest import TestCase
import os


class TestCheapOrchestra(TestCase):
    """Tests for `cheap_orchestra` package."""

    def tearDown(self):
        """Tear Down test files"""
        config_file = '.cheap_orchestra'
        if os.path.exists(config_file):
            os.remove(config_file)

    def test_cli_help(self):
        # given
        runner = CliRunner()
        # when
        help_result = runner.invoke(cli.main, ['--help'])
        # then
        self.assertEqual(0, help_result.exit_code)
        self.assertIn('--help', help_result.output)
        self.assertIn('Show this message and exit.', help_result.output)

    def test_cli_setup_with_all_options_must_create_config_file(self):
        # given
        runner = CliRunner()
        parameters = [
            'setup',
            '--remote_user',
            'ubuntu',
            '--remote_server',
            '10.10.10.1',
            '--private_key',
            'iaeuIUH98IH98G5',
            '--webhook_name',
            'DiscordBot',
            '--webhook_url',
            'https://discordapp.com/api/webhooks/66682398902080/iaeuIUH98IH98G5'
        ]
        # when
        result = runner.invoke(cli.main, parameters)
        # then
        self.assertEqual(0, result.exit_code, result.exc_info)
        with open('.cheap_orchestra', 'r') as file:
            config_file = file.read()
        self.assertIn('CONNECTION:', config_file)
        self.assertIn('REMOTE_USER: ubuntu', config_file)
        self.assertIn('REMOTE_SERVER: 10.10.10.1', config_file)
        self.assertIn('PRIVATE_KEY: iaeuIUH98IH98G5', config_file)
        self.assertIn('WEBHOOK:', config_file)
        self.assertIn('NAME: DiscordBot', config_file)
        self.assertIn('URL: https://discordapp.com/api/webhooks/66682398902080/iaeuIUH98IH98G5', config_file)

    def test_cli_setup_without_optional_args_must_create_config_file(self):
        # given
        runner = CliRunner()
        parameters = [
            'setup',
            '--remote_user',
            'alpine',
            '--remote_server',
            '10.11.10.1',
            '--private_key',
            'iaeuIUH98IH98G5',
        ]
        # when
        result = runner.invoke(cli.main, parameters)
        # then
        self.assertEqual(0, result.exit_code, result.exc_info)
        with open('.cheap_orchestra', 'r') as file:
            config_file = file.read()
        self.assertIn('CONNECTION:', config_file)
        self.assertIn('REMOTE_USER: alpine', config_file)
        self.assertIn('REMOTE_SERVER: 10.11.10.1', config_file)
        self.assertIn('PRIVATE_KEY: iaeuIUH98IH98G5', config_file)
        self.assertNotIn('WEBHOOK:', config_file)
        self.assertNotIn('NAME:', config_file)
        self.assertNotIn('URL:', config_file)

    def test_cli_setup_without_required_remote_user_must_fail(self):
        # given
        runner = CliRunner()
        parameters = [
            'setup',
            '--remote_server',
            '10.10.10.1',
            '--private_key',
            'iaeuIUH98IH98G5',
            '--webhook_name',
            'DiscordBot',
            '--webhook_url',
            'https://discordapp.com/api/webhooks/66682398902080/iaeuIUH98IH98G5'
        ]
        # when
        result = runner.invoke(cli.main, parameters)
        # then
        self.assertEqual(2, result.exit_code, result.exc_info)
        self.assertIn('--remote_user', result.stdout)
