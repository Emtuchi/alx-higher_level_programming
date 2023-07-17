#!/usr/bin/python3
"""Defines a rectangle class"""
import json
from models.base import Base

class Rectangle(Base):
    """Definition of a rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle object of Base"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter o height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x muse be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for x"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def display(self):
        """print the rectangle instance with #"""
        [print("") for i in range(self.__y)]
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()
    
    def __str__(self):
        """Overwrite the string rep of the class"""
        return "[Rectangle] ({:d}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the rectangle"""
        if args:
            for value in range(len(args)):
                if value == 0:
                    if type(args[value]) is not int:
                        raise TypeError("id must be an integer")
                    self.id = args[value]
                elif value == 1:
                    self.width = args[value]
                elif value == 2:
                    self.height = args[value]
                elif value == 3:
                    self.x = args[value]
                elif value == 4:
                    self.y = args[value]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.width == value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of a rectangle"""
        result = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
        return result
