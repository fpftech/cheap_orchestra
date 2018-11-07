from unittest import TestCase
from cheap_orchestra import Configuration
import os


class TestConfiguration(TestCase):
    """Tests for `Configuration` class."""

    def tearDown(self):
        """Tear Down test files"""
        config_file = '.cheap_orchestra'
        if os.path.exists(config_file):
            os.remove(config_file)

    def test_setup_tear_down_without_previous_config_file(self):
        # given
        file = '.cheap_orchestra'
        # when
        Configuration().setup_tear_down()
        # then
        self.assertFalse(os.path.exists(file))

    def test_setup_tear_down_with_previous_config_file(self):
        # given
        orchestra = '.cheap_orchestra'
        config = '''
        CONNECTION: 
          REMOTE_USER: ubuntu
          REMOTE_SERVER: 10.10.10.1
          PRIVATE_KEY: iaueaiIUHiu
        '''
        with open(orchestra, 'w') as file:
            file.write(config)
        # when
        Configuration().setup_tear_down()
        # then
        self.assertFalse(os.path.exists(orchestra))

    def test_persist_connection_setup_with_all_parameters(self):
        # given
        user = 'ubuntu'
        server = '10.10.10.1'
        key = 'iaeuIUH98IH98G5'
        # when
        Configuration().persist_connection_setup(remote_user=user, remote_server=server, private_key=key)
        # then
        with open('.cheap_orchestra', 'r') as file:
            config_file = file.read()
        self.assertIn('REMOTE_USER: ubuntu', config_file)
        self.assertIn('REMOTE_SERVER: 10.10.10.1', config_file)
        self.assertIn('PRIVATE_KEY: iaeuIUH98IH98G5', config_file)

    def test_persist_connection_setup_with_first_wrong_parameter(self):
        # given
        user = 'ubuntu'
        server = '10.10.10.1'
        key = 'iaeuIUH98IH98G5'
        # when then
        with self.assertRaises(TypeError):
            Configuration().persist_connection_setup(remote_user=None, remote_server=server, private_key=key)

    def test_persist_connection_setup_with_second_wrong_parameter(self):
        # given
        user = 'ubuntu'
        server = '10.10.10.1'
        key = 'iaeuIUH98IH98G5'
        # when then
        with self.assertRaises(TypeError):
            Configuration().persist_connection_setup(remote_user=user, remote_server=None, private_key=key)

    def test_persist_connection_setup_with_third_wrong_parameter(self):
        # given
        user = 'ubuntu'
        server = '10.10.10.1'
        key = 'iaeuIUH98IH98G5'
        # when then
        with self.assertRaises(TypeError):
            Configuration().persist_connection_setup(remote_user=user, remote_server=server, private_key=None)

    def test_persist_connection_without_messing_with_other_config(self):
        # given
        orchestra = '.cheap_orchestra'
        config = '''
        WEBHOOK: 
          BOT: DiscordBot
          URL: https://discordapp.com/api/webhooks/66682398902080/iaeuIUH98IH98G5
        '''
        user = 'ubuntu'
        server = '10.10.10.1'
        key = 'iaeuIUH98IH98G5'
        with open(orchestra, 'w') as file:
            file.write(config)
        # when
        Configuration().persist_connection_setup(remote_user=user, remote_server=server, private_key=key)
        # then
        with open('.cheap_orchestra', 'r') as file:
            config_file = file.read()
        self.assertIn('CONNECTION:', config_file)
        self.assertIn('REMOTE_USER: ubuntu', config_file)
        self.assertIn('REMOTE_SERVER: 10.10.10.1', config_file)
        self.assertIn('PRIVATE_KEY: iaeuIUH98IH98G5', config_file)
        self.assertIn('WEBHOOK:', config_file)
        self.assertIn('BOT: DiscordBot', config_file)
        self.assertIn('URL: https://discordapp.com', config_file)

    def test_persist_webhook_setup_with_all_parameters(self):
        # given
        name = 'DiscordBot'
        url = 'https://discordapp.com/api/webhooks/66682398902080/iaeuIUH98IH98G5'
        # when
        Configuration().persist_webhook_setup(name, url)
        # then
        with open('.cheap_orchestra', 'r') as file:
            config_file = file.read()
        self.assertIn('WEBHOOK:', config_file)
        self.assertIn('NAME: DiscordBot', config_file)
        self.assertIn(f'URL: {url}', config_file)
