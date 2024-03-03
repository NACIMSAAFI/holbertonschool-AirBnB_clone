#!/usr/bin/python3
"""
Unit tests for User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_email(self):
        """
        Test User email attribute
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password(self):
        """
        Test User password attribute
        """
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name(self):
        """
        Test User first_name attribute
        """
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name(self):
        """
        Test User last_name attribute
        """
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
