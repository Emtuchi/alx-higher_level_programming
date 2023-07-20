#!/usr/bin/python3
"""Creates a class square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Defines a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a class square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width
    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update class"""
        if args is not None and len(args) != 0:
            for value in range(len(args)):
                if value == 0:
                    if type(args[value]) is not int:
                        raise TypeError("id must be an integer")
                    self.id = args[value]
                elif value == 1:
                    self.size = args[value]
                elif value == 2:
                    self.x = args[value]
                elif value == 3:
                    self.y = args[value]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return dictionary representation of a square"""
        dic_t = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            }
        return dic_t
