#!/usr/bin/python3
"""
Console module
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User


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
        """Creates a new instance of BaseModel and saves it to JSON"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name != "BaseModel":
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
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all()
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")


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
            if class_name != "BaseModel":
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
        if class_name != "BaseModel":
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
