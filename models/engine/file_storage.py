#!/usr/bin/python3
"""
Module that contains the FileStorage class.

This class serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import json
from datetime import datetime


class FileStorage():
    """ Serializes instances to a JSON file
    and deserializes JSON file to instances. """
    __file_path = "file.json"
    __objects = {}  # Will store all objects by <class name>.id

    def all(self):
        """ Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key `<obj class name>.id`. """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path). """
        objects = {}
        for key, obj in self.__objects.items():
            objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.

        This method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists otherwise, do nothing.
        If the file doesn't exist, no exception is raised).
        """
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
            for value in data.values():
                if 'created_at' in value:
                    value['created_at'] = datetime.fromisoformat(
                        value['created_at'])
                if 'updated_at' in value:
                    value['updated_at'] = datetime.fromisoformat(
                        value['updated_at'])
                class_name = value['__class__']
                # Get the class object dynamically
                class_obj = globals()[class_name]
                obj = class_obj(**value)
                self.new(obj)

        except FileNotFoundError:
            pass
