#!/usr/bin/python3
"""Module that contain Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class that inherits from BaseMode"""
    place_id = ""
    user_id = ""
    text = ""
