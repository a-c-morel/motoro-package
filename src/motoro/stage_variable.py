__wind_strenght = 0
__wind_time = 0
__wind_cooldown = 0
__gravity_strengh = 1

class StageVariable():

    @staticmethod
    @property
    def wind_strenght() -> int:
        return __wind_strenght

    @staticmethod
    @wind_strenght.setter
    def wind_strenght(value :int ) -> None:
        __wind_strenght = value

    @staticmethod
    @property
    def wind_time() -> int:
        return __wind_time

    @staticmethod
    @wind_time.setter
    def wind_time(value :int ) -> None:
        __wind_time = value

    @staticmethod
    @property
    def wind_cooldown() -> int:
        return __wind_cooldown

    @staticmethod
    @wind_cooldown.setter
    def wind_cooldown(value :int ) -> None:
        __wind_cooldown = value

    @staticmethod
    @property
    def gravity_strengh() -> int:
        return __gravity_strengh

    @staticmethod
    @gravity_strengh.setter
    def gravity_strengh(value :int ) -> None:
        __gravity_strengh = value
