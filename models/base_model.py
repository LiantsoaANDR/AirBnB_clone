#!/usr/bin/python3
"""
Module for our base of all other class models in this project
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    This is the 'base' class of all other models in this project

    Attributes:
        id:  string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime
                    when an instance is created
        updated_at: datetime - assign with the current datetime
                    when an instance is created and it will be updated
                    every time you change your object
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the new BaseModel object

        Args:
            *args: won't be used
            **kwargs: dict of the value of our attributes
        """
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    frm = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(value, frm)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """
        Return the representation of how BaseModel should be printed
        """
        name = self.__class__.__name__
        return ("[{}] ({}) {}".format(name, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict
