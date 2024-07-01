#!/usr/bin/python3
"""Module for testing City class using unittests"""
import models


class TestCity(unittest.TestCase):
    """Tests the City class"""

    def test_city_initialization(self):
        """Tests City"""
       city_instance = City()
       self.assertEqual(state_instance.state_id, "")
       self.assertEqual(state_instance.name, "")
