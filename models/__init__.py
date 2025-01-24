#!/usr/bin/python3
""" init magic method. """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
