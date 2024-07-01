#!/usr/bin/python3
"""Module that contains the entry point of the command interpreter"""
import cmd
import models
import shlex

class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb) '
    __classes = ["BaseModel"]
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
        if not arg:
            print("** class name missing **")
        
        class_name = arg.split()[0]
        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[class_name]()
            new_instance.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
