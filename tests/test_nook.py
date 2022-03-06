#!/usr/bin/env python

"""Tests for `nook` package."""


import unittest

from nook import nook


class TestNook(unittest.TestCase):
    """Tests for `nook` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_hello_prefix_name_with_welcome(self):
        """Test something."""
        self.assertEqual(nook.hello("nook"), 'welcome nook', 'prefix name with string hello')
