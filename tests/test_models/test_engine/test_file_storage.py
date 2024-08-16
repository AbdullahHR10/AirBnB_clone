#!/usr/bin/python3
"""Module that contains unittests for FileStorage class"""
import unittest
import models
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unittests that tests FileStorage class"""

    def setUp(self):
        """Sets up environment for tests"""
        self.instance = FileStorage()

    def test_kwargs_initialization(self):
        """Tests initialization with kwargs"""
        pass

    def test_no_kwargs_initialization(self):
        """Tests initialization without kwargs"""
        pass

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
        basemodel = BaseModel()
        models.storage.new(basemodel)
        self.assertIn("BaseModel." + basemodel.id, models.storage.all().keys())
        self.assertIn(basemodel, models.storage.all().values())

    def test_save(self):
        """Tests save method"""
        basemodel = BaseModel()
        models.storage.new(basemodel)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as file:
            save_text = file.read()
            self.assertIn("BaseModel." + basemodel.id, save_text)


if __name__ == "__main__":
    unittest.main()
