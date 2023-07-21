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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert to json strings"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json string to a file"""
        if (type(list_objs) != list and
           list_objs is not None or
           not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")
        
        n_file = cls.__name__ + ".json"
        with open(n_file, "w") as _file:
            if list_objs is None:
                _file.write("[]")
            else:
               dicts = [objs.to_dictionary() for objs in list_objs]
               _file.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with all attributes set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as _file:
                dicts = cls.from_json_string(_file.read())
                new_list = [cls.create(**ls) for ls in dicts]
                return new_list
        except IOError:
            return []
