#!/usr/bin/python3
"""Module that contains the console"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User"]

    def do_quit(self, line):
        """Exits the program"""
        return True

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """Handles empty lines"""
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        arg = parse(line)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            all_objects = storage.all()
            if key in all_objects:
                instance = all_objects[key]
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            all_objects = storage.all()
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        args = parse(line)
        all_objects = storage.all()
        instances = []
        if len(args) == 0:
            for obj in all_objects.values():
                instances.append(str(obj))
        elif len(args) == 1:
            class_name = args[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, obj in all_objects.items():
                if key.startswith(class_name + '.'):
                    instances.append(str(obj))
        print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instance_id = args[1]
            attr_name = args[2]
            attr_value = args[3]
            key = f"{class_name}.{instance_id}"
            all_objects = storage.all()
            if key in all_objects:
                instance = all_objects[key]
                setattr(instance, attr_name, attr_value)
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
