from abc import ABC

class EntityVariable(ABC):
    def __init_subclass__(self,
            max_mometum_x : int = 4,
            initial_value_mometum_x : int = -1.1,
            increasse_mometum_x : int = 0.5,
            loose_mometum_x : int = 0.25,
            initial_jump_mometum : int = 1.36,
            initial_jump_gain : int = 1.125,
            increase_jump_gain : int = 0.125,
            max_jump_gain : int = 1.5) -> None:
        self.__max_mometum_x : int = max_mometum_x
        self.__initial_value_mometum_x : int = initial_value_mometum_x
        self.__increasse_mometum_x : int = increasse_mometum_x
        self.__loose_mometum_x : int = loose_mometum_x
        self.__initial_jump_mometum : int = initial_jump_mometum
        self.__initial_jump_gain : int = initial_jump_gain
        self.__increase_jump_gain : int = increase_jump_gain
        self.__max_jump_gain : int = max_jump_gain

    @property
    def max_mometum_x(self)-> int:
        return self.__max_mometum_x

    @max_mometum_x.setter
    def max_mometum_x(self, value: int)-> None:
        self.__max_mometum_x = value

    @property
    def initial_value_mometum_x(self)-> int:
        return self.__initial_value_mometum_x

    @initial_value_mometum_x.setter
    def initial_value_mometum_x(self, value: int)-> None:
        self.__initial_value_mometum_x = value

    @property
    def increasse_mometum_x(self)-> int:
        return self.__increasse_mometum_x

    @increasse_mometum_x.setter
    def increasse_mometum_x(self, value)-> None:
        self.__increasse_mometum_x = value

    @property
    def loose_mometum_x(self)-> int:
        return self.__loose_mometum_x

    @loose_mometum_x.setter
    def loose_mometum_x(self, value: int)-> None:
        self.__loose_mometum_x = value

    @property
    def initial_jump_mometum(self)-> int:
        return self.__initial_jump_mometum

    @initial_jump_mometum.setter
    def initial_jump_mometum(self, value: int)-> None:
        self.__initial_jump_mometum = value

    @property
    def initial_jump_gain(self)-> int:
        return self.__initial_jump_gain

    @initial_jump_gain.setter
    def initial_jump_gain(self, value: int)-> None:
        self.__initial_jump_gain = value

    @property
    def increase_jump_gain(self)-> int:
        return self.__increase_jump_gain

    @increase_jump_gain.setter
    def increase_jump_gain(self, value: int)-> None:
        self.__increase_jump_gain = value

    @property
    def max_jump_gain(self)-> int:
        return self.__max_jump_gain

    @max_jump_gain.setter
    def max_jump_gain(self, value: int)-> None:
        self.__max_jump_gain = value
