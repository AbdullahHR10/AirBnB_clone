#!/usr/bin/python3
"""Module for testing Amenity class"""
from models.amenity import Amenity

class TestUser(unittest.TestCase):
    """Tests the User class"""

    def test_user_initialization(self):
        """Test initialization of Amenity class"""
        amenity_instance = Amenity()
        self.assertEqual(state_instance.name, "")
