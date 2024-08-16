#!/usr/bin/python3
"""Module that contains unittests for BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests that tests BaseModel class"""

    def setUp(self):
        """Sets up environment for tests"""
        self.instance = BaseModel()
        kwargs = {
            "id": "123",
            "created_at": "2005-04-03T05:30:00.000000",
            "updated_at": "2005-04-03T05:30:00.000000",
        }
        self.kwargs_instance = BaseModel(**kwargs)

    def test_kwargs_initialization(self):
        """Tests initialization with kwargs"""
        self.assertEqual(self.kwargs_instance.id, "123")
        self.assertEqual(self.kwargs_instance.created_at.isoformat(),
                         "2005-04-03T05:30:00")
        self.assertEqual(self.kwargs_instance.updated_at.isoformat(),
                         "2005-04-03T05:30:00")

    def test_no_kwargs_initialization(self):
        """Tests initialization without kwargs"""
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_attributes(self):
        """Tests attributes"""
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_str(self):
        """Tests __str__ method"""
        string_rep = str(self.instance)
        expected = f"[BaseModel] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(string_rep, expected)   

    def test_save(self):
        """Tests save method"""
        old_updated_at = self.instance.updated_at
        self.instance.save()
        self.assertIsInstance(self.instance.updated_at, datetime)
        self.assertNotEqual(self.instance.updated_at, old_updated_at)

    def test_dict(self):
        """Tests to_dict method"""
        instance_dict = self.instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)             


if __name__ == "__main__":
    unittest.main()
