import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestHBNBCommand(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment"""
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after tests"""
        storage._FileStorage__objects = {}

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_place(self, mock_stdout):
        """Test the create command for Place"""
        HBNBCommand().onecmd("create Place")
        obj_id = list(storage.all().values())[0].id
        self.assertTrue(f"Place.{obj_id}" in storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_user(self, mock_stdout):
        """Test the create command for User"""
        HBNBCommand().onecmd("create User")
        obj_id = list(storage.all().values())[0].id
        self.assertTrue(f"User.{obj_id}" in storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_state(self, mock_stdout):
        """Test the create command for State"""
        HBNBCommand().onecmd("create State")
        obj_id = list(storage.all().values())[0].id
        self.assertTrue(f"State.{obj_id}" in storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_place(self, mock_stdout):
        """Test Place.update("id", "attribute_name", "string_value")"""
        HBNBCommand().onecmd("create Place")
        obj_id = list(storage.all().values())[0].id
        HBNBCommand().onecmd(f'update Place {obj_id} name "Villa"')
        self.assertEqual(storage.all()[f"Place.{obj_id}"].name, "Villa")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_user(self, mock_stdout):
        """Test User.update("id", "attribute_name", "string_value")"""
        HBNBCommand().onecmd("create User")
        obj_id = list(storage.all().values())[0].id
        HBNBCommand().onecmd(f'update User {obj_id} email "user@example.com"')
        self.assertEqual(storage.all()[f"User.{obj_id}"].email, "user@example.com")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_state(self, mock_stdout):
        """Test State.update("id", "attribute_name", "string_value")"""
        HBNBCommand().onecmd("create State")
        obj_id = list(storage.all().values())[0].id
        HBNBCommand().onecmd(f'update State {obj_id} name "California"')
        self.assertEqual(storage.all()[f"State.{obj_id}"].name, "California")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_city(self, mock_stdout):
        """Test the destroy command for City"""
        HBNBCommand().onecmd("create City")
        obj_id = list(storage.all().values())[0].id
        HBNBCommand().onecmd(f"destroy City {obj_id}")
        self.assertNotIn(f"City.{obj_id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_amenity(self, mock_stdout):
        """Test the count command for Amenity"""
        HBNBCommand().onecmd("create Amenity")
        HBNBCommand().onecmd("create Amenity")
        HBNBCommand().onecmd("count Amenity")
        self.assertEqual(mock_stdout.getvalue().strip(), "2")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_review(self, mock_stdout):
        """Test the show command for Review"""
        HBNBCommand().onecmd("create Review")
        obj_id = list(storage.all().values())[0].id
        HBNBCommand().onecmd(f"show Review {obj_id}")
        output = mock_stdout.getvalue().strip()
        self.assertIn(obj_id, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_amenity_with_dict(self, mock_stdout):
        """Test update with a dictionary for Amenity"""
        HBNBCommand().onecmd("create Amenity")
        obj_id = list(storage.all().values())[0].id
        HBNBCommand().onecmd(f'update Amenity {obj_id} {{"name": "Pool", "description": "Large"}}')
        self.assertEqual(storage.all()[f"Amenity.{obj_id}"].name, "Pool")
        self.assertEqual(storage.all()[f"Amenity.{obj_id}"].description, "Large")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_review(self, mock_stdout):
        """Test the create command for Review"""
        HBNBCommand().onecmd("create Review")
        obj_id = list(storage.all().values())[0].id
        self.assertTrue(f"Review.{obj_id}" in storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_review(self, mock_stdout):
        """Test Review.update("id", "attribute_name", "string_value")"""
        HBNBCommand().onecmd("create Review")
        obj_id = list(storage.all().values())[0].id
        HBNBCommand().onecmd(f'update Review {obj_id} text "Amazing stay"')
        self.assertEqual(storage.all()[f"Review.{obj_id}"].text, "Amazing stay")


if __name__ == "__main__":
    unittest.main()

