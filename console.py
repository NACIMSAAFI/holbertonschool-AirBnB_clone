#!/usr/bin/python3
"""
Console module
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    my_classes = ["BaseModel", "User", "State", "City",
                  "Amenity", "Place", "Review"]

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
        """
        Create a new instance of BaseModel and save it to the JSON file.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.my_classes:
            print("** class doesn't exist **")
        else:
            instance = eval(f"{args[0]}()")
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.my_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
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
        class_name = args[0]
        if class_name not in self.my_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
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
        """Prints all string representation of all instances
        based or not on the class name"""
        args = shlex.split(arg)
        if not args:
            all_objs = storage.all()
            for obj in all_objs.values():
                print(obj)
            return
        if len(args) < 2:
            class_name = args[0]
            if class_name not in self.my_classes:
                print("** class doesn't exist **")
                return
        all_objs = storage.all()
        for key, obj in all_objs.items():
            if class_name in key:
                print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.my_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
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
        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** can't update attribute **")
            return
        setattr(all_objs[key_to_search], attribute_name, attribute_value)
        all_objs[key_to_search].save()
        print(all_objs[key_to_search])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
