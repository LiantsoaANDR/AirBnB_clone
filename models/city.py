#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel


class city(BaseModel):
    """
    City, a class that inherits from BaseModel

    Attributes:
            state_id: The state id from State.id
            name: the name of the city
    """
    state_id = ""
    name = ""
