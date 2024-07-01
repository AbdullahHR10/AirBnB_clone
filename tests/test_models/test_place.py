#!/usr/bin/python3
"""Module for testing State class using unittests"""
from models.Place import Place


class TestPlace(unittest.TestCase):
    """Tests the Place class"""
    def test_state_initialization(self):
        """Test initialization of Place class"""
        place_instance = Place()
        self.assertEqual(place_instance.city_id, "")
        self.assertEqual(place_instance.user_id, "")
        self.assertEqual(place_instance.name, "")
        self.assertEqual(place_instance.description, "")
        self.assertEqual(place_instance.number_rooms, 0)
        self.assertEqual(place_instance.number_bathrooms, 0)
        self.assertEqual(place_instance.max_guest, 0)
        self.assertEqual(place_instance.price_by_night, 0)
        self.assertAlmostEqual(place_instance.latitude, 0.0)
        self.assertAlmostEqual(place_instance.longitude, 0.0)
        self.assertEqual(place_instance.amenity_ids, [])
