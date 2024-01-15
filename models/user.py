#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User, a class that inherits from BaseModel

    Attributes:
        email: user's email
        password: user's password
        first_name: user's first_name
        last_name: user's last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
