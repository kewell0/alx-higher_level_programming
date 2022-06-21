#!/usr/bin/python3
"""3-square.py - A module that contains a Square class"""


class Square:
    """defines a square by:
    - private instance variable: size
    - Instantiation with optional size
    """

    def __init__(self, size=0):
        """Initialize the instance attribute"""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a new value for the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square to the screen"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
