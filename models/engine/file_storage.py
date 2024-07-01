#!/usr/bin/python3
"""Module for FileStorage class"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
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
                    elif cls_name == 'State':
                        cls = State
                    elif cls_name == 'City':
                        cls = City
                    elif cls_name == 'Amenity':
                        cls = Amenity
                    elif cls_name == 'Place':
                        cls = Place
                    elif cls_name == 'Review':
                        cls = Review
                    else:
                        cls = globals()[cls_name]
                    self.new(cls(**value))
        except FileNotFoundError:
            pass
