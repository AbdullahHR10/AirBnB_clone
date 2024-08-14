#!/usr/bin/python3
"""Module that contains unittests for User class"""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unittests that tests User class"""

    def setUp(self):
        """Sets up environment for tests"""
        self.instance = User()
        kwargs = {
            "id": "123",
            "created_at": "2005-04-03T05:30:00.000000",
            "updated_at": "2005-04-03T05:30:00.000000",
            "email": "user@email.com",
            "password": "abc123",
            "first_name": "First",
            "last_name": "Last"
        }
        self.kwargs_instance = User(**kwargs)

    def test_kwargs_initialization(self):
        """Tests initialization with kwargs"""
        self.assertEqual(self.kwargs_instance.id, "123")
        self.assertEqual(self.kwargs_instance.created_at.isoformat(),
                         "2005-04-03T05:30:00")
        self.assertEqual(self.kwargs_instance.updated_at.isoformat(),
                         "2005-04-03T05:30:00")
        self.assertEqual(self.kwargs_instance.email, "user@email.com")
        self.assertEqual(self.kwargs_instance.password, "abc123")
        self.assertEqual(self.kwargs_instance.first_name, "First")
        self.assertEqual(self.kwargs_instance.last_name, "Last")

    def test_no_kwargs_initialization(self):
        """Tests initialization without kwargs"""
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_inheritance(self):
        """Tests if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Tests attributes"""
        self.assertIsInstance(self.instance.email, str)
        self.assertIsInstance(self.instance.password, str)
        self.assertIsInstance(self.instance.first_name, str)
        self.assertIsInstance(self.instance.last_name, str)
        self.assertEqual(self.instance.email, "")
        self.assertEqual(self.instance.password, "")
        self.assertEqual(self.instance.first_name, "")
        self.assertEqual(self.instance.last_name, "")

    def test_dict(self):
        """Tests to_dict method"""
        instance_dict = self.instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], 'User')
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)

    def test_str(self):
        """Tests __str__ method"""
        string_rep = str(self.instance)
        expected = f"[User] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(string_rep, expected)


if __name__ == "__main__":
    unittest.main()
