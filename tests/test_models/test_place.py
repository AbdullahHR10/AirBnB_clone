#!/usr/bin/python3
"""Module that contains unittests for Place class"""
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Unittests that tests Place class"""

    def setUp(self):
        """Sets up environment for tests"""
        self.instance = Place()
        kwargs = {
            "id": "123",
            "created_at": "2005-04-03T05:30:00.000000",
            "updated_at": "2005-04-03T05:30:00.000000",
            "city_id": "456",
            "user_id": "789",
            "name": "Place",
            "description": "This is a place",
            "number_rooms": 3,
            "number_bathrooms": 2,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 12.34,
            "longitude": 56.78,
            "amenity_ids": ["321", "654", "987"]
        }
        self.kwargs_instance = Place(**kwargs)

    def test_kwargs_initialization(self):
        """Tests initialization with kwargs"""
        self.assertEqual(self.kwargs_instance.id, "123")
        self.assertEqual(self.kwargs_instance.created_at.isoformat(),
                         "2005-04-03T05:30:00")
        self.assertEqual(self.kwargs_instance.updated_at.isoformat(),
                         "2005-04-03T05:30:00"),
        self.assertEqual(self.kwargs_instance.city_id, "456")
        self.assertEqual(self.kwargs_instance.user_id, "789")
        self.assertEqual(self.kwargs_instance.name, "Place")
        self.assertEqual(self.kwargs_instance.description, "This is a place")
        self.assertEqual(self.kwargs_instance.number_rooms, 3)
        self.assertEqual(self.kwargs_instance.number_bathrooms, 2)
        self.assertEqual(self.kwargs_instance.max_guest, 4)
        self.assertEqual(self.kwargs_instance.price_by_night, 100)
        self.assertEqual(self.kwargs_instance.latitude, 12.34)
        self.assertEqual(self.kwargs_instance.longitude, 56.78)
        self.assertEqual(self.kwargs_instance.amenity_ids, ["321",
                                                            "654", "987"])

    def test_no_kwargs_initialization(self):
        """Tests initialization without kwargs"""
        self.assertIsNotNone(self.instance)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_inheritance(self):
        """Tests if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """Tests attributes"""
        self.assertIsInstance(self.instance.name, str)
        self.assertIsInstance(self.instance.description, str)
        self.assertIsInstance(self.instance.number_rooms, int)
        self.assertIsInstance(self.instance.number_bathrooms, int)
        self.assertIsInstance(self.instance.max_guest, int)
        self.assertIsInstance(self.instance.price_by_night, int)
        self.assertIsInstance(self.instance.latitude, float)
        self.assertIsInstance(self.instance.longitude, float)
        self.assertIsInstance(self.instance.amenity_ids, list)
        self.assertEqual(self.instance.name, "")
        self.assertEqual(self.instance.description, "")
        self.assertEqual(self.instance.number_rooms, 0)
        self.assertEqual(self.instance.number_bathrooms, 0)
        self.assertEqual(self.instance.max_guest, 0)
        self.assertEqual(self.instance.price_by_night, 0)
        self.assertEqual(self.instance.latitude, 0.0)
        self.assertEqual(self.instance.longitude, 0.0)
        self.assertEqual(self.instance.amenity_ids, [])

    def test_dict(self):
        """Tests to_dict method"""
        instance_dict = self.instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], 'Place')
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertIn('city_id', instance_dict)
        self.assertIn('user_id', instance_dict)
        self.assertIn('name', instance_dict)
        self.assertIn('description', instance_dict)
        self.assertIn('number_rooms', instance_dict)
        self.assertIn('number_bathrooms', instance_dict)
        self.assertIn('max_guest', instance_dict)
        self.assertIn('price_by_night', instance_dict)
        self.assertIn('latitude', instance_dict)
        self.assertIn('longitude', instance_dict)
        self.assertIn('amenity_ids', instance_dict)

    def test_str(self):
        """Tests __str__ method"""
        string_rep = str(self.instance)
        expected = f"[Place] ({self.instance.id}) {self.instance.__dict__}"
        self.assertEqual(string_rep, expected)


if __name__ == "__main__":
    unittest.main()
