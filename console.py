#!/usr/bin/python3
"""Module that contains the entry point of the command interpreter"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb) '

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
        if class_name not in storage.classes:
        print("** class doesn't exist **")
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
