from abc import ABC, abstractmethod

# Classes are a core concept in OOP
# Abstraction: Hide unnecessary details
# and expose only what is needed.
# An abstract class is a class that 
# cannot be instantiated directly.
# It is used to define a common interface
# that all child classes must follow.

# Object vs. Instance - 

class Character(ABC):
    """Base Abstract Class"""
    def __init__(self, first_name, is_alive=True):
        """Class self Constructor"""
        self.first_name = first_name # self refers to instance
        self.is_alive = is_alive

    @classmethod # method will be shared by all instances
                 # makes the class to call the method without,
                 # initing the object
    @abstractmethod
    def die(cls):
        """function to die"""
        pass

class Stark(Character):
    """Your docstring for Class"""
    def die(self):
        """Your docstring for method"""
        self.is_alive = False
    
        