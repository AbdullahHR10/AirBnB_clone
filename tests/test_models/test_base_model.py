#!/usr/bin/python3
"""Module for testing BaseModel class using unittests"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests BaseModel."""
    def setUp(self):
        """Sets up data for tests"""
        self.instance = BaseModel(
                id='123',
                created_at=datetime.datetime(2024, 6, 29, 10, 0, 0),
                updated_at=datetime.datetime(2024, 6, 29, 12, 0, 0),
                name='Abdullah Hussein',
                age=19
                )

    def test_str_representation(self):
        """Tests the __str__ method"""
        expected_str = "[BaseModel](123) {'id': '123', 'created_up:
                                          '2024-06-29T10:00:00', 'updated_at':
                                          '2024-06-29T12:00:00', 'name':
                                          'Abdullah Hussein', 'age': 19}"
        self.assertEqual(str(self.instance), expected_str)

    def test_save(self):
        """Tests the save method"""
        first_updated_at = self.instance.updated_at
        self.instance.name = 'Abdullah Hussein Ragab'
        self.instance.save()
        self.assertNotEqual(first_updated_at, self.instance.updated_at)

    def test_to_dict(self):
        """Tests the to_dict method"""
        expected_dict = {
                'id': '123',
                'created_at': '2024-06-29T10:00:00',
                'updated_at': self.instance.updated_at.isoformat(),
                'name': 'Abdullah Hussein',
                'age': 19,
                '__class__': 'BaseModel'
                }
        instance_dict = self.instance.to_dict()
        self.assertEqual(instance_dict, expected_dict)

    def test_id(self):
        """Tests the id attribute"""
        self.assertIsInstance(self.instance.id, str)

    def test_created_at(self):
        """Tests the created_at attribute"""
        self.assertIsInstance(self.instance.created_at, datetime.datetime)
        expected_created_at = datetime.datetime(2024, 6, 29, 10, 0, 0)
        self.assertEqual(self.instance.created_at, expected_created_at)


if __name__ == '__main__':
    unittest.main()
