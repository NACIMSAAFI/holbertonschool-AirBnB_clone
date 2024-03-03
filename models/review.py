from models.base_model import BaseModel

""" A class Review that inherits from BaseModel"""


class Review(BaseModel):
    """Represents a review."""

    place_id = ""
    user_id = ""
    text = ""
