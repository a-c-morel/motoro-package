"""module contenant la classe StageVariable"""
from abc import ABC

class StageVariable(ABC): #pylint: disable=too-few-public-methods
    """Class representing the variables of the stage."""

    wind_strength: int  = 0
    wind_time: int = 0
    wind_cooldown: int = 0
    gravity_strengh: int = 1

    def __new__(cls, *args, **kwargs):
        raise TypeError("the class StageVariable can't be instancied.")

    def __init_subclass__(cls, *args, **kwargs):
        raise TypeError('this class cannot be inherited')
