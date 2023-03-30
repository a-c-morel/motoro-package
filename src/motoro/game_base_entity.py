"""this module contain the base class for entity"""
import math
from typing import Iterable, Literal
from abc import ABC, abstractmethod
import pygame
from .game_raw_entity import GameRawEntity
from .stage_variable import StageVariable
from .game_base_bloc import GameBaseBloc

class GameBaseEntity(GameRawEntity, ABC):
    """
    base class for game entity
    this class is abstract
    therfor you can never create an object with it !
    """
    def __new__(cls, *args, **kwargs):
        if cls is GameBaseEntity:
            raise TypeError("the abstarct class GameBaseEntity can't be instancied.")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, coords : Iterable[int]) -> None:
        if not isinstance(coords, tuple) and not isinstance(coords, list):
            raise TypeError(f'coords should be Iterable object got {type(coords)}')
        if i:=len(coords) != 2:
            raise ValueError(f'coords should have 2 element got {i}')
        if not isinstance(coords[0], int) or not isinstance(coords[1], int):
            raise TypeError(
                f'coords should only conataint int object got \
                    {type(coords[0])} and {type(coords[1])}')
        if coords[0] < 0 or coords[1] < 0:
            raise TypeError(
                f'coords should only conataint int object >= 0 got {coords[0]} and {coords[1]}')
        self.momentum_x : float = 0.0
        self.sprites : list[pygame.Surface]
        self.current_frame : pygame.Surface
        super().__init__(coords)

    def go_left(self, blocs: list[GameBaseBloc]) -> None:
        """make the entity go left and gain mometum"""
        if not isinstance(blocs, list):
            raise TypeError(f'block should be a list object got {type(blocs)}')
        for i in blocs:
            if not isinstance(i, GameBaseBloc):
                raise TypeError(f'block should only contain GameBaseBloc instance got {type(i)}')
        self.old_coords[0] = self.coords[0]
        if self.momentum_x == 0:
            self.momentum_x = -self.initial_value_mometum_x
        elif self.momentum_x > -self.max_mometum_x:
            self.momentum_x -= self.increasse_mometum_x
        self.coords[0] += int(self.momentum_x)
        self._old_rect_hitbox = self.rect_hitbox
        self._hitbox_calculation()
        while True:
            tmp = self.collision(blocs, bool(self.momentum_y<0))
            if tmp[0]:
                return
            if tmp[1] == -1:
                return
            self.coords[0] = tmp[1].right+1
            self.momentum_x = 0

    def go_right(self, blocs) -> None:
        """make the entity go right and gain mometum"""
        if not isinstance(blocs, list):
            raise TypeError(f'block should be a list object got {type(blocs)}')
        for i in blocs:
            if not isinstance(i, GameBaseBloc):
                raise TypeError(f'block should only contain GameBaseBloc instance got {type(i)}')
        if self.momentum_x == 0:
            self.momentum_x = self.initial_value_mometum_x
        elif self.momentum_x < self.max_mometum_x:
            self.momentum_x +=self.increasse_mometum_x
        self.coords[0] += int(self.momentum_x)
        self._old_rect_hitbox = self.rect_hitbox
        self._hitbox_calculation()
        while True:
            tmp = self.collision(blocs, bool(self.momentum_y<0))
            if tmp[0]:
                return None
            if tmp[1] == -1:
                return self.death_seqeunce('crush')
            self.coords[0] = tmp[1].left - self.hitbox_dimension[0]-1
            self.momentum_x = 0

    def sliding(self, blocs) -> None:
        """make the entity 'slide' with mometum it as"""
        if not isinstance(blocs, list):
            raise TypeError(f'block should be a list object got {type(blocs)}')
        for i in blocs:
            if not isinstance(i, GameBaseBloc):
                raise TypeError(f'block should only contain GameBaseBloc instance got {type(i)}')
        if self.momentum_x == 0:
            return None
        self.old_coords[0] = self.coords[0]
        self.coords[0] += int(self.momentum_x)
        self._old_rect_hitbox = self.rect_hitbox
        self._hitbox_calculation()
        if self.momentum_x < 0:
            while True:
                tmp = self.collision(blocs, bool(self.momentum_y<0))
                if tmp[0]:
                    break
                if tmp[1] == -1:
                    return self.death_seqeunce('crush')
                self.coords[0] = tmp[1].left -self.hitbox_dimension[0]
                self.momentum_x = 0
                self._hitbox_calculation()
        else:
            while True:
                tmp = self.collision(blocs, bool(self.momentum_y<0))
                if tmp[0]:
                    break
                if tmp[1] == -1:
                    return self.death_seqeunce('crush')
                self.coords[0] = tmp[1].right
                self.momentum_x = 0
                self._hitbox_calculation()

    def passive(self, blocs : list[GameBaseBloc], clock : pygame.time.Clock) -> Literal[-1] | None:
        """
        all the 'passive' action of the entity
        like : loosing momentum, making him subjext to gravity
        """
        if not isinstance(clock, pygame.time.Clock):
            raise TypeError(f'clock should be a pygame.time.Clock object got {type(clock)}')
        if not isinstance(blocs, list):
            raise TypeError(f'block should be a list object got {type(blocs)}')
        for i in blocs:
            if not isinstance(i, GameBaseBloc):
                raise TypeError(f'block should only contain GameBaseBloc instance got {type(i)}')
        if i:=StageVariable.wind_time+StageVariable.wind_cooldown != 0:
            if clock.get_time()%i >= StageVariable.wind_cooldown:
                self.momentum_x += StageVariable.wind_strength
        if self.momentum_x <= 1 and self.momentum_x >= -1:
            self.momentum_x = 0.0
        else:
            self.momentum_x -= math.copysign(self.loose_mometum_x, self.momentum_x)
        return super().base_passive(blocs)

    def render(self, screen : pygame.surface.Surface, offset_x : int = 0, offset_y : int = 0) -> None:
        """render the entity on the screen"""
        if not isinstance(screen, pygame.surface.Surface):
            raise TypeError(f'screen should be a pygame.surface.Surface object got {type(screen)}')
        if not isinstance(offset_x, int):
            raise TypeError(f'offset_x should be a int object got {type(offset_x)}')
        if not isinstance(offset_y, int):
            raise TypeError(f'offset_x should be a int object got {type(offset_y)}')
        screen.blit(self.current_frame, (self.coords[0] + offset_x, self.coords[1] + offset_y))

    @abstractmethod
    def death_seqeunce(self, origin: str):
        """this function handle the death of a entity"""
        raise NotImplementedError

    @abstractmethod
    def interaction(self, __o : 'GameBaseEntity'):
        """a method to handle interaction with other entity (collission)"""
        raise NotImplementedError
