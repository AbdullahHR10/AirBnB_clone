#!/usr/bin/python3
"""Module that contains unittests for City class"""
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unittests that tests City class"""

    def setUp(self):
        """Sets up environment for tests"""
        self.instance = City()
        kwargs = {
            "id": "123",
            "created_at": "2005-04-03T05:30:00.000000",
            "updated_at": "2005-04-03T05:30:00.000000",
            "state_id": "456",
            "name": "Cairo"
        }
        self.kwargs_instance = City(**kwargs)

    def test_kwargs_initialization(self):
        """Tests initialization with kwargs"""
        self.assertEqual(self.kwargs_instance.id, "123")
        self.assertEqual(self.kwargs_instance.created_at.isoformat(),
                         "2005-04-03T05:30:00")
        self.assertEqual(self.kwargs_instance.updated_at.isoformat(),
                         "2005-04-03T05:30:00")
        self.assertEqual(self.kwargs_instance.state_id, "456")
        self.assertEqual(self.kwargs_instance.name, "Cairo")

    def test_no_kwargs_initialization(self):
        """Tests initialization without kwargs"""
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_inheritance(self):
        """Tests if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Tests attributes"""
        self.assertIsInstance(self.instance.state_id, str)
        self.assertIsInstance(self.instance.name, str)

    def test_dict(self):
        """Tests to_dict method"""
        instance_dict = self.instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], 'City')
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)

    def test_str(self):
        """Tests __str__ method"""
        string_rep = str(self.instance)
        expected = f"[City] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(string_rep, expected)


if __name__ == "__main__":
    unittest.main()
