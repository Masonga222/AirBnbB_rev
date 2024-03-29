#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone
"""

import json
import models


class FileStorage:
    """
    Serializes instances to JSON file and deserializes to JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Return the dictionary
        """

        if not cls:
            return self.__objects
        else:
            new = {obj: key for obj, key in self.__objects.items()
                   if type(key) is cls}
            return new

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        """

        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        Serializes __objects attribute to JSON file.
        """

        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """

        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it’s inside
        """

        FileStorage.__objects = {
            key: value for key,
            value in FileStorage.__objects.items() if value != obj}

    def close(self):
        self.reload()
