#1/usr/bin/python3
"""
Module serialize and deserialize JSON file and storage
"""

import json


class FileStorage():
	"""
	A class that serializes instances to a
	JSON file and deserializes JSON file to instances
	"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        A method returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        A method sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        A method serializes __objects to the JSON file (path: __file_path)
        """
        dict_save = {}
        with open(self.__file_path, "w+", encoding="UTF-8") as f:
        for key, value in self.__objects.items():
            dict_save[key] = value
            json.dump(dict_save, f)
           