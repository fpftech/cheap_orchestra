# -*- coding: utf-8 -*-
from slugify import slugify
import yaml
"""Main module."""


class Maestro:
    def __init__(self, compose_file):
        self.compose_file = compose_file
        with open(compose_file, 'r') as file:
            self.compose_dict = yaml.load(file)

    def append_service_name(self, service_name, suffix):
        new_name = slugify('{0}-{1}'.format(service_name, suffix))
        self.compose_dict["services"][new_name] = self.compose_dict["services"].pop(service_name)
        return self.compose_dict
