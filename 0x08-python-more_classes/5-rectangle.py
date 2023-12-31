#!/usr/bin/python3

"""Defines the rectangle."""

class Rectangle:
    """Represents a recntangle."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle.

        Args:
            width as an int.
            height as an int.
        """
    
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Gets the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """Gets the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.height * 2))

    def area(self):
        """Gets the area."""
        return (self.__width * self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        print("Bye rectangle...")
