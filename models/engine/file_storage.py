#!/usr/bin/python3
"""Module for FileStorage class"""

from models.base_model import BaseModel
from models.user import User
import json


class FileStorage:
    """
    Class thatSerializes instances to a JSON file and deserializes
    JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dictionary): Stores all objects by <class name>.id
        """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict() for key,
                    obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name = value['__class__']
                    if cls_name == 'BaseModel':
                        cls = BaseModel
                    elif cls_name == 'User':
                        cls = User
                    else:
                        cls = globals()[cls_name]
                    self.new(cls(**value))
        except FileNotFoundError:
            pass
