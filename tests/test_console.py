import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment"""
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after tests"""
        storage._FileStorage__objects = {}

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test the create command"""
        self.assertFalse(storage.all())  # No instances initially
        HBNBCommand().onecmd("create BaseModel")
        self.assertTrue(len(storage.all()) > 0)  # Instance should be created
        output = mock_stdout.getvalue().strip()
        self.assertRegex(output, r'^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$')  # Check UUID format

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test the show command"""
        HBNBCommand().onecmd("create BaseModel")
        obj_id = list(storage.all().values())[0].id
        HBNBCommand().onecmd(f"show BaseModel {obj_id}")
        output = mock_stdout.getvalue().strip()
        self.assertIn(obj_id, output)
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class(self, mock_stdout):
        """Test show command with missing class"""
        HBNBCommand().onecmd("show")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_instance_not_found(self, mock_stdout):
        """Test show command when instance is not found"""
        HBNBCommand().onecmd("show BaseModel 1234")
        self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Test the destroy command"""
        HBNBCommand().onecmd("create BaseModel")
        obj_id = list(storage.all().values())[0].id
        HBNBCommand().onecmd(f"destroy BaseModel {obj_id}")
        self.assertEqual(len(storage.all()), 0)
        HBNBCommand().onecmd(f"show BaseModel {obj_id}")
        self.assertEqual(mock_stdout.getvalue().strip(), "** no instance found **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test the all command"""
        HBNBCommand().onecmd("create BaseModel")
        HBNBCommand().onecmd("all BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertIn("BaseModel", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """Test the update command"""
        HBNBCommand().onecmd("create BaseModel")
        obj_id = list(storage.all().values())[0].id
        HBNBCommand().onecmd(f'update BaseModel {obj_id} name "Test"')
        self.assertEqual(storage.all()[f"BaseModel.{obj_id}"].name, "Test")

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        """Test the count command"""
        HBNBCommand().onecmd("create BaseModel")
        HBNBCommand().onecmd("create BaseModel")
        HBNBCommand().onecmd("count BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "2")

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_command(self, mock_stdout):
        """Test unknown command"""
        HBNBCommand().onecmd("unknowncommand")
        self.assertEqual(mock_stdout.getvalue().strip(), "*** Unknown syntax: unknowncommand")

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Test help command"""
        HBNBCommand().onecmd("help")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Documented commands", output)


if __name__ == "__main__":
    unittest.main()
