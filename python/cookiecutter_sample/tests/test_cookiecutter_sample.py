#!/usr/bin/env python

"""Tests for `cookiecutter_sample` package."""


import unittest

from cookiecutter_sample import cookiecutter_sample as cs


class TestCookiecutter_sample(unittest.TestCase):
    """Tests for `cookiecutter_sample` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_doit(self):
        self.assertEqual(1, cs.doit(None))
