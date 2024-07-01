#!/usr/bin/python3
"""Module for testing City class using unittests"""
from models.city import City


class TestCity(unittest.TestCase):
    """Tests the City class"""
    def test_city_initialization(self):
        """Test initialization of State class"""
        city_instance = City()
        self.assertEqual(state_instance.state_id, "")
        self.assertEqual(state_instance.name, "")
