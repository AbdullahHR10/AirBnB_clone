#!/usr/bin/python3
"""Module that contains the console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """Handles empty lines"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
