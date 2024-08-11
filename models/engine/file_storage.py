#!/usr/bin/python3
"""Module that contains FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                    elif class_name == "User":
                        obj = User(**value)
                    elif class_name == "State":
                        obj = State(**value)
                    elif class_name == "City":
                        obj = City(**value)
                    elif class_name == "Amenity":
                        obj = Amenity(**value)
                    elif class_name == "Place":
                        obj = Place(**value)
                    elif class_name == "Review":
                        obj = Review(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
