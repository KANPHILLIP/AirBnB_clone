#!/usr/bin/python3
""" module for the base model of all the classes """
import uuid
import datetime

class BaseModel:
    """ BaseModel class where all other classes will
    inherit from
    """
    def __init__(self, *args, **kwargs):
        """ intitializes intstances attributes
        Args:
        *args: (tuple of arguments)
        **kwargs: {dict key-value arguments}
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()


