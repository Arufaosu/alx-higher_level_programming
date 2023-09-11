#!/usr/bin/python3
"""defines a base geometry class BaseGeometry"""

class BaseGeometry:
    """represents base geometry"""

    def area(self):
        """not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a parameter as an integer

        Args:
            name: name of the parameter
            value: parameter to validate
        Raises:
            TypeError: value is not an integer
            ValueError: value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
