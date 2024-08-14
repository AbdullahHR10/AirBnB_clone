#!/usr/bin/python3
"""Module that contains unittests for Review class"""
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Unittests that tests Review class"""

    def setUp(self):
        """Sets up environment for tests"""
        self.instance = Review()
        kwargs = {
            "id": "123",
            "created_at": "2005-04-03T05:30:00.000000",
            "updated_at": "2005-04-03T05:30:00.000000",
            "place_id": "123",
            "user_id": "456",
            "text": "This is text"
        }
        self.kwargs_instance = Review(**kwargs)

    def test_kwargs_initialization(self):
        """Tests initialization with kwargs"""
        self.assertEqual(self.kwargs_instance.id, "123")
        self.assertEqual(self.kwargs_instance.created_at.isoformat(),
                         "2005-04-03T05:30:00")
        self.assertEqual(self.kwargs_instance.updated_at.isoformat(),
                         "2005-04-03T05:30:00")
        self.assertEqual(self.kwargs_instance.place_id, "123")
        self.assertEqual(self.kwargs_instance.user_id, "456")
        self.assertEqual(self.kwargs_instance.text, "This is text")

    def test_no_kwargs_initialization(self):
        """Tests initialization without kwargs"""
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_inheritance(self):
        """Tests if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Tests attributes"""
        self.assertIsInstance(self.instance.place_id, str)
        self.assertIsInstance(self.instance.user_id, str)
        self.assertIsInstance(self.instance.text, str)
        self.assertEqual(self.instance.place_id, "")
        self.assertEqual(self.instance.user_id, "")
        self.assertEqual(self.instance.text, "")

    def test_dict(self):
        """Tests to_dict method"""
        instance_dict = self.instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], 'Review')
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)

    def test_str(self):
        """Tests __str__ method"""
        string_rep = str(self.instance)
        expected = f"[Review] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(string_rep, expected)


if __name__ == "__main__":
    unittest.main()
