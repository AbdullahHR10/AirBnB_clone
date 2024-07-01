#!/usr/bin/python3
"""Module for testing State class using unittests"""
from models.review import Reivew


class TestReview(unittest.TestCase):
    """Tests Review"""
    def test_reiew_initialization(self):
        """Test initialization of Review class"""
        review_instance = Review()
        self.assertEqual(review_instance.place_id, "")
        self.assertEqual(review_instance.user_id, "")
        self.assertEqual(review_instance.text, "")
