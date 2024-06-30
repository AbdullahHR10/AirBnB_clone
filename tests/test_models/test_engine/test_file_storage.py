#!/usr/bin/python3
"""Module to test FileStorage class"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_stroage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class to test FileStorage"""
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        """Tests the all method"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)


if __name__ == '__main__':
    unittest.main()
