#!/usr/bin/python3
"""serializes instances to JSON file and deserializes JSON file to instances"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """New class"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """returns dict"""
        return self.__objects

    def new(self, obj):
        """sets in __objects dict a new obj"""
        a = obj.__class__.__name__
        self.__objects[a + "." + obj.id] = obj

    def save(self):
        """serializes"""
        new = {}
        for key, value in self.__objects.items():
            new.update([(key, value.to_dict())])
        with open(self.__file_path, "w+") as fil:
            json.dump(new, fil)

    def pop(self, key):
        '# pop objects'
        self.__objects.pop(key)

    def reload(self):
        """ deserializes the JSON file"""
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, "r") as fil:
                copy = json.load(fil)
            for y, o in copy.items():
                self.__objects[y] = eval(o["__class__"])(**o)

    @staticmethod
    def class_list():
        """list of all classes"""
        return ["BaseModel", "User", "City", "Amenity", "Place", "Review"]
