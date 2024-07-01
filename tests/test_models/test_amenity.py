#!/usr/bin/python3
"""Module for testing Amenity class"""
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Tests the Amenity class"""

    def test_Amenity_initialization(self):
        """Test initialization of Amenity class"""
        amenity_instance = Amenity()
        self.assertEqual(state_instance.name, "")
