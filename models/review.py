#!/usr/bin/python3
"""Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review, a class that inherits from BaseModel

    Attributes:
            place_id: Place.id
            user_id: User.id
            text: the review
    """
    place_id = ""
    user_id = ""
    text = ""
