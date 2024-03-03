#!/usr/bin/python3
"""
Unit tests for City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_name(self):
        """
        Test City name attribute
        """
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
