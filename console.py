#!/usr/bin/python3
"""Module that contains the console"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parse(line):
    """Parses the input line into a list of arguments."""
    return line.strip().split()


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter"""
    prompt = "(hbnb) "
    classes = ["BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"
               ]

    def default(self, line):
        """Default behavior for cmd module when input is invalid"""
        commands_dict = {
                "all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy
                }
        if '.' in line:
            try:
                class_name, rest = line.split('.', 1)
                method_name, args = rest.split('(', 1)
                args = args.strip(')')
            except ValueError:
                print(f"*** Unknown syntax: {line}")
                return
            class_name, method = line.split('.')
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            if method_name in commands_dict:
                if method_name in ["all", "count"]:
                    commands_dict[method_name](class_name)
                elif method_name in ["show", "destroy"]:
                    if args:
                        line = f"{class_name} {args}"
                        commands_dict[method_name](line)
                    else:
                        print("** instance id missing **")
                        return
                else:
                    print(f"** unknown method {method_name} **")
            else:
                print(f"** unknown method {method} **")
        else:
            print(f"*** Unknown syntax: {line}")

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

    def do_count(self, line):
        """Retrieves the number of instances of a class"""
        args = parse(line)
        i = 0
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            count = 0
            all_objects = storage.all()
            for key in all_objects:
                if key.startswith(class_name + '.'):
                    count += 1
            print(count)

    def do_show(self, line):
        """Retrieves an instance based on its ID"""
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            key = f"{class_name}.{instance_id}"
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            else:
                print(all_objects[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
