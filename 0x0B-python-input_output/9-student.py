#!/usr/bin/python3
"""defines a class called student"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """initialises a new student

        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
