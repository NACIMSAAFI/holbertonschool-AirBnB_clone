#!/usr/bin/python3
"""
Console module
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage

my_classes = [
    "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class and saves it to JSON"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in my_classes:
            print("** class doesn't exist **")
            return
        cls = getattr(__import__('models'), class_name)
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in my_classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        key_to_search = class_name + "." + instance_id
        all_objs = storage.all()
        if key_to_search not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key_to_search])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in my_classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        key_to_search = class_name + "." + instance_id
        all_objs = storage.all()
        if key_to_search not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key_to_search]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = shlex.split(arg)
        if not args:
            all_objs = storage.all()
            for obj in all_objs.values():
                print(obj)
            return
        class_name = args[0]
        if class_name not in my_classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        for key, obj in all_objs.items():
            if key.split('.')[0] == class_name:
                print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in my_classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        key_to_search = class_name + "." + instance_id
        all_objs = storage.all()
        if key_to_search not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        setattr(all_objs[key_to_search], attribute_name, attribute_value)
        all_objs[key_to_search].save()
        print(all_objs[key_to_search])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
