#!/usr/bin/python3
"""Module that contains FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instance"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    if class_name == 'BaseModel':
                        obj = BaseModel(**value)
                    else:
                        continue
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
