#!/usr/bin/python3
"""Module for testing State class using unittests"""
from models.state import State


class TestState(unittest.TestCase):
    """Tests State"""
    def test_state_initialization(self):
        """Test initialization of State class"""
        state_instance = State()
        self.assertEqual(state_instance.name, "")
