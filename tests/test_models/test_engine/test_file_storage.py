#!/usr/bin/python3
"""Module that contains unittests for FileStorage class"""
import unittest
import models
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unittests that tests FileStorage class"""

    def setUp(self):
        """Sets up environment for tests"""
        models.storage = FileStorage()
        self.instance = BaseModel()

    def test_attributes(self):
        """Tests attributes"""
        self.assertIsInstance(self.instance.__file_path, str)
        self.assertIsInstance(self.instance.__objects, dict)
        self.assertEqual(self.instance.__file_path, "file.json")
        self.assertEqual(self.instance.__objects, {})

    def test_all(self):
        """Tests all method"""
        dict_instance = self.instance.all()
        self.assertIsInstance(dict_instance, dict)

    def test_new(self):
        """Tests new method"""
        self.storage.new(self.instance)
        key = f"{self.instance.__class__.__name__}.{self.instance.id}"
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[key],
                         self.instance)

    def test_save(self):
        """Tests save method"""
        models.storage.new(self.instance)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as file:
            save_text = file.read()
            self.assertIn(f"{self.instance.__class__}" +
                          self.instance.id, save_text)

    def test_reload(self):
        """Tests reload method"""
        models.storage.new(self.instance)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn(f"{self.instance.__class__.__name__}" +
                      self.instance.id, objs)


if __name__ == "__main__":
    unittest.main()
