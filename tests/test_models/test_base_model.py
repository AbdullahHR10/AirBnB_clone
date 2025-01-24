#!/usr/bin/python3
""" Module that contains BaseModel class unittests. """

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """ Unittests for the BaseModel class. """
    def setUp(self):
        """ Sets up any state or objects for the tests. """
        self.obj = BaseModel()
        self.kwargs = {
            "id": "123abc",
            "created_at": "2025-01-24T12:00:00",
            "updated_at": "2025-01-24T12:05:00",
            "__class__": "BaseModel"
        }
        self.kwargs_obj = BaseModel(**self.kwargs)

    def test_attributes(self):
        """ Tests BaseModel attributes without kwargs. """
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertEqual(self.obj.__class__.__name__, "BaseModel")

    def test_attributes_with_kwargs(self):
        """ Tests BaseModel attributes with kwargs. """
        self.assertEqual(self.kwargs_obj.id, "123abc")
        self.assertEqual(self.kwargs_obj.created_at,
                         datetime(2025, 1, 24, 12, 0, 0))
        self.assertEqual(self.kwargs_obj.updated_at,
                         datetime(2025, 1, 24, 12, 5, 0))
        self.assertEqual(self.kwargs_obj.__class__.__name__, "BaseModel")

    def test_save_method(self):
        """ Tests save method. """
        previous_updated_at = self.obj.updated_at
        sleep(0.1)
        self.obj.save()
        self.assertNotEqual(self.obj.updated_at, previous_updated_at)

    def test_dict_method(self):
        """ Tests dict method. """
        obj_dict = self.obj.to_dict()
        self.assertIsInstance(obj_dict, dict)

        # Check if the dictionary contains the expected keys
        self.assertIn("id", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)
        self.assertIn("__class__", obj_dict)

        # Check if the types of the values are correct
        self.assertIsInstance(obj_dict["id"], str)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_str_method(self):
        """ Tests __str__ method. """
        expected_str = f"[{self.obj.__class__.__name__}] " \
                       f"({self.obj.id}) {self.obj.__dict__}"
        self.assertEqual(str(self.obj), expected_str)

    def tearDown(self):
        """ Cleans up any state or object after the tests. """
        del self.obj
        del self.kwargs_obj
