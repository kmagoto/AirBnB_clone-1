#!/usr/bin/python3

import models
from datetime import datetime
from uuid import uuid4

"""
Module BaseModel
Parent of all classes
"""

class BaseModel():
    """Base class for Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """


    def __init__(self, *args, **kwargs):
        """
        Initializes attributes: random uuid, dates created/updated

        """
        if kwargs: