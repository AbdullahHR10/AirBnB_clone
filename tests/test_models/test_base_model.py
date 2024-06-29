#!/usr/bin/python3
"""Module for testing BaseModel class using unittests"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.Testcase):
    """Tests BaseModel."""
    def test_save(self):
        """Tests the method save."""
        instance = BaseModel()
        instance.save()
        self.assertNotEqual(instance.created_at, instance.updated_at)


if __name__ == '__main__':
    unittest.main()
