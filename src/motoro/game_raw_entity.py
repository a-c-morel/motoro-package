"""this module contain the "raw" class for entity"""
from abc import ABC
from .game_base_object import GameBaseObject

class GameRawEntity(GameBaseObject, ABC): #pylint: disable=too-many-instance-attributes
    """represent the proprety and base instance of an entity"""

    def __new__(cls, *args, **kwargs):
        if cls is GameRawEntity:
            raise TypeError("the abstarct class GameRawEntity can't be instancied.")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, #pylint: disable=too-many-arguments
            coord,
            max_mometum_x : float = 4.0,
            initial_value_mometum_x : float = 1.1,
            increasse_mometum_x : float = 0.5,
            loose_mometum_x : float = 0.25,
            initial_jump_mometum : float = 1.36,
            initial_jump_gain : float = 1.125,
            increase_jump_gain : float = 0.125,
            max_jump_gain : float = 1.5,) -> None:
        self._max_mometum_x : float = max_mometum_x
        self._initial_value_mometum_x : float = initial_value_mometum_x
        self._increasse_mometum_x : float = increasse_mometum_x
        self._loose_mometum_x : float = loose_mometum_x
        self._initial_jump_mometum : float = initial_jump_mometum
        self._initial_jump_gain : float = initial_jump_gain
        self._increase_jump_gain : float = increase_jump_gain
        self._max_jump_gain : float = max_jump_gain
        super().__init__(coord)

    @property
    def max_mometum_x(self)-> float:
        """proprety of the max mometum x"""
        return self._max_mometum_x

    @max_mometum_x.setter
    def max_mometum_x(self, value: float)-> None:
        if not isinstance(value, float):
            raise TypeError(f'value should be float got {type(value)}')
        if value < 1.0:
            raise ValueError(f'value should be >= 1.0 got {value}')
        self._max_mometum_x = value

    @property
    def initial_value_mometum_x(self)-> float:
        """proprety of the initial mometum x"""
        return self._initial_value_mometum_x

    @initial_value_mometum_x.setter
    def initial_value_mometum_x(self, value: float)-> None:
        if not isinstance(value, float):
            raise TypeError(f'value should be float got {type(value)}')
        if value < 1.0:
            raise ValueError(f'value should be >= 1.0 got {value}')
        self._initial_value_mometum_x = value

    @property
    def increasse_mometum_x(self)-> float:
        """proprety of the increasse mometum x"""
        return self._increasse_mometum_x

    @increasse_mometum_x.setter
    def increasse_mometum_x(self, value)-> None:
        if not isinstance(value, float):
            raise TypeError(f'value should be float got {type(value)}')
        if value < 1.0:
            raise ValueError(f'value should be >= 1.0 got {value}')
        self._increasse_mometum_x = value

    @property
    def loose_mometum_x(self)-> float:
        """proprety of the loose mometum x"""
        return self._loose_mometum_x

    @loose_mometum_x.setter
    def loose_mometum_x(self, value: float)-> None:
        if not isinstance(value, float):
            raise TypeError(f'value should be float got {type(value)}')
        if value < 1.0:
            raise ValueError(f'value should be >= 1.0 got {value}')
        self._loose_mometum_x = value

    @property
    def initial_jump_mometum(self)-> float:
        """proprety of the initial jump mometum"""
        return self._initial_jump_mometum

    @initial_jump_mometum.setter
    def initial_jump_mometum(self, value: float)-> None:
        if not isinstance(value, float):
            raise TypeError(f'value should be float got {type(value)}')
        if value < 1.0:
            raise ValueError(f'value should be >= 1.0 got {value}')
        self._initial_jump_mometum = value

    @property
    def initial_jump_gain(self)-> float:
        """proprety of the gain jump mometum"""
        return self._initial_jump_gain

    @initial_jump_gain.setter
    def initial_jump_gain(self, value: float)-> None:
        if not isinstance(value, float):
            raise TypeError(f'value should be float got {type(value)}')
        if value < 1.0:
            raise ValueError(f'value should be >= 1.0 got {value}')
        self._initial_jump_gain = value

    @property
    def increase_jump_gain(self)-> float:
        """proprety of the increase gain jump mometum"""
        return self._increase_jump_gain

    @increase_jump_gain.setter
    def increase_jump_gain(self, value: float)-> None:
        if not isinstance(value, float):
            raise TypeError(f'value should be float got {type(value)}')
        if value < 1.0:
            raise ValueError(f'value should be >= 1.0 got {value}')
        self._increase_jump_gain = value

    @property
    def max_jump_gain(self)-> float:
        """proprety of the max gain jump mometum"""
        return self._max_jump_gain

    @max_jump_gain.setter
    def max_jump_gain(self, value: float)-> None:
        if not isinstance(value, float):
            raise TypeError(f'value should be float got {type(value)}')
        if value < 1.0:
            raise ValueError(f'value should be >= 1.0 got {value}')
        self._max_jump_gain = value
