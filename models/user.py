#!/usr/bin/python3
""" A class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the system."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
