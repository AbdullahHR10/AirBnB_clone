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

    def test_new(self):
        """Tests the new method"""
        new_obj = self.storage.new()
        self.assertTrue(hasattr(new_obj, 'id'))

    def test_save(self):
        """Tests the save method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Tests the reload method"""
        initial_objects = {'obj1': {'id': '1', 'name': 'Object 1'},
                           'obj2': {'id': '2', 'name': 'Object 2'}}
        with open(self.test_file, 'w') as f:
            json.dump(initial_objects, f)
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(self.storage.all(), initial_objects)

    def test_objects_attribute(self):
        """Tests the __objects attribute directly"""
        obj1 = {'id': '1', 'name': 'Object 1'}
        obj2 = {'id': '2', 'name': 'Object 2'}
        self.storage._FileStorage__objects['obj1'] = obj1
        self.storage._FileStorage__objects['obj2'] = obj2
        self.assertEqual(self.storage._FileStorage__objects['obj1'], obj1)
        self.assertEqual(self.storage._FileStorage__objects['obj2'], obj2)


if __name__ == '__main__':
    unittest.main()
