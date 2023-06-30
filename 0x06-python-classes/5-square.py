#!/usr/bin/python3

"""Create a class square"""

class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Make size a property."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print to stdout the square with #."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
