#!/usr/bin/env python3

class Shoe:
    # Constructor method that initializes the attributes of a Shoe object
    # Key concept: Constructor (__init__ method)
    def __init__(self, brand, size):
        # Assigning the 'brand' parameter to the 'brand' attribute of the object
        # Key concept: Instance variables
        self.brand = brand
        
        # Assigning the 'size' parameter to the 'size' attribute of the object
        # Key concept: Instance variables
        self.size = size
        
        # Assigning the string "Old" to the 'condition' attribute of the object
        # Key concept: Instance variables
        self.condition = "Old"

    # Property decorator that defines a getter method for the 'size' attribute
    # Key concept: Properties and getters
    @property
    def size(self):
        # Returning the value of the private '_size' attribute
        # Key concept: Instance variables (private)
        return self._size

    # Setter method for the 'size' attribute
    # Key concept: Properties and setters
    @size.setter
    def size(self, value):
        # Checking if the 'value' parameter is an instance of the 'int' class
        # Key concept: Type checking
        if not isinstance(value, int):
            # If 'value' is not an integer, print an error message
            # Key concept: Print statements
            print("size must be an integer")
        else:
            # If 'value' is an integer, assign it to the private '_size' attribute
            # Key concept: Instance variables (private)
            self._size = value

    # Instance method that represents the cobbling (repairing) of a shoe
    # Key concept: Instance methods
    def cobble(self):
        # Assigning the string "New" to the 'condition' attribute of the object
        # Key concept: Instance variables
        self.condition = "New"
        
        # Printing a message indicating that the shoe has been repaired
        # Key concept: Print statements
        print("Your shoe is as good as new!")