#!/usr/bin/python3
"""Module that contains the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb) '
    valid_classes = {"BaseModel"}
    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program"""
        return True

    def do_help(self, arg):
        """Provides help information about available commands"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Does nothing when getting an empty line input"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            if args[0] == "BaseModel":
                new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
