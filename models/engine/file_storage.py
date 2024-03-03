#!/usr/bin/python3
import json
import os



class FileStorage:
    """
    manages serialization and deserialization of objects
    and from JSON files.
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Adds an object to the __objects dictionary.
        """
        obj_name = obj.__class__.__name__
        key = "{}.{}".format(obj_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def save(self):
        """
        Serializes __objects to a JSON file.
        """
        objects = self.__objects
        dic_data = {}
        for i in objects.keys():
            dic_data[i] = objects[i].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dic_data, f)

    def reload(self):
        """
        Deserializes JSON file to __objects.
        """
        from models.base_model import BaseModel
        from models.user import User

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    dic_data = json.load(f)
                    for key, value in dic_data.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass