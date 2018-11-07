#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cheap_orchestra` package."""

from cheap_orchestra import Maestro, Configuration
from unittest import TestCase
import os


class TestMaestro(TestCase):
    """Tests for `Maestro` class."""

    def setUp(self):
        """Set up test fixtures, if any."""
        base_folder = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_folder, "docker-compose.yml")
        self.maestro = Maestro(path)

    def test_append_service_name_with_front_and_suffix_a_must_create_front_suffix_a_key(self):
        # given
        service_name = "front"
        suffix_name = "suffix-a"
        final_name = "front-suffix-a"
        # when
        maestro = self.maestro.append_service_name(service_name, suffix_name)
        # then
        self.assertIsNotNone(maestro.compose_dict["services"].get(final_name))

    def test_append_service_name_with_front_and_suffix_a_must_delete_front_key(self):
        # given
        service_name = "front"
        suffix_name = "suffix-a"
        # when
        maestro = self.maestro.append_service_name(service_name, suffix_name)
        # then
        self.assertIsNone(maestro.compose_dict["services"].get(service_name))

    def test_append_service_name_with_api_and_hiffen_suffix_b_must_create_api_suffix_b_key(self):
        # given
        service_name = "api"
        suffix_name = "-suffix_b"
        final_name = "api-suffix-b"
        # when
        maestro = self.maestro.append_service_name(service_name, suffix_name)
        # then
        self.assertIsNotNone(maestro.compose_dict["services"].get(final_name))

    def test_append_service_name_with_database_and_slash_suffix_c_must_create_database_suffix_c_key(self):
        # given
        service_name = "database"
        suffix_name = "/suffix_c"
        final_name = "database-suffix-c"
        # when
        maestro = self.maestro.append_service_name(service_name, suffix_name)
        # then
        self.assertIsNotNone(maestro.compose_dict["services"].get(final_name))

    def test_append_service_name_with_database_and_backslash_suffix_c_must_create_database_suffix_c_key(self):
        # given
        service_name = "database"
        suffix_name = "\suffix_c"
        final_name = "database-suffix-c"
        # when
        maestro = self.maestro.append_service_name(service_name, suffix_name)
        # then
        self.assertIsNotNone(maestro.compose_dict["services"].get(final_name))

    def test_append_service_name_with_first_invalid_parameter(self):
        # given
        suffix_name = "\suffix_c"
        # when then
        with self.assertRaises(TypeError):
            self.maestro.append_service_name(None, suffix_name)

    def test_append_service_name_with_second_invalid_parameter(self):
        # given
        service_name = "database"
        # when then
        with self.assertRaises(TypeError):
            self.maestro.append_service_name(service_name, None)

    def test_append_service_name_with_invalid_parameters(self):
        # given when then
        with self.assertRaises(TypeError):
            self.maestro.append_service_name(None, None)
