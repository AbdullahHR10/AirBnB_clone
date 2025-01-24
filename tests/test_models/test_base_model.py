#!/usr/bin/python3
""" Module that contains BaseModel class unittests. """

import unittest
from models.base_model import BaseModel
from datetime import datetime


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

    def tearDown(self):
        """ Cleans up any state or object after the tests. """
        del self.obj
        del self.kwargs_obj
