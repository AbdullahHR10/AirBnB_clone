#!/usr/bin/python3
"""Module for testing User class"""
import unittest
import models


class TestUser(unittest.TestCase):
    """Tests the User class"""

    def test_user_initialization(self):
        """Test initialization of User class"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
