#!/usr/bin/python3
"""Place module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place, a class that inherits from BaseModel

    Attributes:
            city_id: the City.id
            user_id: the User.id
            name: its name
            description: description of the place
            number_rooms: the number of rooms
            number_bathrooms: the number of bathrooms
            max_guest: the max guest
            price_by_night: the price of a night
            latitude: the latitude of where is the place
            longitude: the longitude of where the place
            amenity_ids: Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
