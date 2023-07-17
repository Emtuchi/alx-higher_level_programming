#!/usr/bin/python3
"""Creating a base class"""

import json

class Base:
    """Create a base definition"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base.
        Args:
           id (int): The identity of the base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
