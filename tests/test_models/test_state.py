#!/usr/bin/python3
"""
Unit tests for State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_name(self):
        """
        Test State name attribute
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
