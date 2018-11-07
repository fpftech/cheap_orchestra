# -*- coding: utf-8 -*-
from slugify import slugify
import yaml
import os
"""Main module."""


class Maestro:

    def __init__(self, compose_file: str):
        """
        Builds a new Maestro instance.
        It loads a docker-compose file into a memory structure so you can
        orchestrate your changes.
        :param compose_file: a valid string path to a docker-compose file.
        """
        if type(compose_file) is not str:
            raise TypeError("Maestro needs a valid compose_file path string!")
        self.compose_file = compose_file
        with open(compose_file, 'r') as file:
            self.compose_dict = yaml.load(file)

    def append_service_name(self, service_name: str, suffix: str) -> 'Maestro':
        """
        It manipulates the name of a given service that is part of the loaded
        docker-compose file.
        :param service_name: The name of the service as described in the docker-compose file.
        :param suffix: A string to be transformed into a slug and appended to the service name.
        :return: the same Maestro instance so you can chain several calls
        """
        if type(service_name) is not str or type(suffix) is not str:
            raise TypeError("Maestro.append_service_name needs a valid service_name and suffix strings!")
        new_name = slugify('{0}-{1}'.format(service_name, suffix))
        self.compose_dict["services"][new_name] = self.compose_dict["services"].pop(service_name)
        return self


class Configuration:
    """
    This Class performs the persistent Orchestra configuration using a config file.
    The default is .cheap_orchestra but you can set anything you like.
    """

    def __init__(self, file='.cheap_orchestra'):
        self.config_file = file

    def persist_connection_setup(self, remote_user: str, remote_server: str, private_key: str):
        """
        This method persists the connection information in the object configuration file.
        :param remote_user: User that will be used to connect in the remote server
        :param remote_server: The remote server dns or ip
        :param private_key: The private ssh key used to connect to the remote host
        :return: None
        """
        if not all(type(arg) is str for arg in (remote_user, remote_server, private_key)):
            raise TypeError('remote_user, remote_server and private_key must all be valid strings!')
        config = self.load_existing_setup()
        config['CONNECTION'] = {
                'REMOTE_USER': remote_user,
                'REMOTE_SERVER': remote_server,
                'PRIVATE_KEY': private_key
                }
        result = yaml.dump(config, default_flow_style=False)
        with open(self.config_file, 'w') as file:
            file.write(result)

    def persist_webhook_setup(self, webhook_name: str, webhook_url: str):
        """
        This method persists the webhook information in the object configuration file.
        :param webhook_name: Discord bot name
        :param webhook_url: URL to make the request
        :return: None
        """
        if not all(type(arg) is str for arg in (webhook_name, webhook_url)):
            raise TypeError('webhook_name and webhook_url must all be valid strings!')
        config = self.load_existing_setup()
        config['WEBHOOK'] = {
                'NAME': webhook_name,
                'URL': webhook_url
                }
        result = yaml.dump(config, default_flow_style=False)
        with open(self.config_file, 'w') as file:
            file.write(result)

    def setup_tear_down(self):
        """Remove config file if any."""
        if os.path.exists(self.config_file):
            os.remove(self.config_file)

    def load_existing_setup(self):
        """
        Loads the configuration file to return the a dictionary containing the setup.
        :return: setup dict or an empty dict
        """
        if not os.path.exists(self.config_file):
            return dict()
        with open(self.config_file, 'r') as file:
            text = file.read()
        return yaml.load(text)
