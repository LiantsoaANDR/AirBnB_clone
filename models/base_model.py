#!/usr/bin/python3
"""
Module for our base of all other class models in this project
"""
from datetime import datetime
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
    id = str(uuid.uuid4())
    created_at = datetime.today()
    updated_at = datetime.today()

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict
