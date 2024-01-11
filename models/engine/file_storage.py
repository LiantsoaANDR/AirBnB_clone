#!/usr/bin/python3
"""Module for file storage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Class that serves to  serialize instances to a JSON file and
    deserialize JSON file to instances

    Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects:  dictionary - empty but will store all objects by
                    <class name>.id (ex: to store a BaseModel object
                    with id=12121212, the key will be BaseModel.12121212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objetcs

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        Saves all the objets into a JSON with the objet dictionaries
        """
        obj_dict = {}
        for key, value in FileStorage.__objetcs.items():
            obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                object_dict = json.load(f)
                for key in object_dict:
                    self.__objects[key] = BaseModel(**object_dict[key])
        except FileNotFoundError:
            pass
