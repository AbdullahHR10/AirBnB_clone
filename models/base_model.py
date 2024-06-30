#!/usr/bin/python3
"""Module for the base model"""
import uuid
import datetime
import models


class BaseModel():
    """
    Class that defines all common attributes/methods for other classes.

    Attributes:
        id (str): A unique identifier for each instance.
        created_at (str): The timestamp when the instance was created.
        updated_at (str): The timestamp when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes MyClass with a unique ID, creation, and update timestamps.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at:
        With the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary:
        Containing all keys/values of __dict__ of the instance.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
