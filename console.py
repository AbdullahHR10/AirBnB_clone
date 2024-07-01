#!/usr/bin/python3
"""Module that contains the entry point of the command interpreter"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb) '
    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def do_help(self, line):
        """Provides help information about available commands"""
        cmd.Cmd.do_help(self, line)

    def emptyline(self):
        """Does nothing when getting an empty line input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
