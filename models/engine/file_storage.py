#!/usr/bin/python3

"""
    FileStorage module
"""

import json
from os.path import exists


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as file:
            json.dump({
                key: obj.to_dict() for key, obj in self.__objects.items()},
                file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel

        if exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    class_ = eval(class_name)
                    self.__objects[key] = class_(**value)
