#!/usr/bin/python3
"""
Module that contains the BaseModl class.

This class defines all common attributes/methods for all other classes
in the website.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ Defines all common attributes/methods for other classes. """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Parameters:
            args: Positional arguments.
            kwargs: Keyword arguments.
        """
        if kwargs:
            # Loop through kwargs items
            for key, value in kwargs.items():
                if key != "__class__":
                    # Check if the key needs to be iso formated
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """ Updates `updated_at` attribute with the current datetime. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Provides a dictionary representation containing all keys and values
        of the instance

        Returns:
            A dictionary containing all keys/values of __dict__
            of the instance.
        """
        dict_representation = {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__
        }
        return dict_representation

    def __str__(self):
        """
        Provides a human-readable representation of the object

        Returns:
            A string represntation of the BaseModel object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
