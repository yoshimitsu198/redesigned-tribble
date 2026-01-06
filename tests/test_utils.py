"""
Unit tests for utility functions.
"""

import unittest
from utils import format_message, validate_input

class TestUtils(unittest.TestCase):
    
    def test_format_message(self):
        self.assertEqual(format_message("hello"), "Hello")
        self.assertEqual(format_message("  test  "), "Test")
    
    def test_validate_input(self):
        self.assertTrue(validate_input("valid"))
        self.assertFalse(validate_input(""))
        self.assertFalse(validate_input(None))



# add_edge_tests - additional commit 4
