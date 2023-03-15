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
    def __init__(self, coords : Iterable) -> None:
        self.momentum_x : float = 0.0
        self.sprites : Iterable
        super().__init__(coords)

    def go_left(self, blocs: list[GameBaseBloc]) -> None:
        """make the entity go left and gain mometum"""
        self.old_coords[0] = self.coords[0]
        if self.momentum_x == 0:
            self.momentum_x = -self.initial_value_mometum_x
        elif self.momentum_x > -self.max_mometum_x:
            self.momentum_x -= self.increasse_mometum_x
        self.coords[0] += int(self.momentum_x)
        if self.coords[0] < 0:
            self.coords[0] = 0
            self.momentum_x = 0
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
        if self.momentum_x == 0:
            self.momentum_x = self.initial_value_mometum_x
        elif self.momentum_x < self.max_mometum_x:
            self.momentum_x +=self.increasse_mometum_x
        self.coords[0] += int(self.momentum_x)
        if self.coords[0] > 500:
            self.coords[0] = 500
            self.momentum_x = 0
        self._hitbox_calculation()
        while True:
            tmp = self.collision(blocs, bool(self.momentum_y<0))
            if tmp[0]:
                return
            if tmp[1] == -1:
                return
            self.coords[0] = tmp[1].left - self.hitbox_dimension[0]-1
            self.momentum_x = 0

    def sliding(self, blocs) -> None:
        """make the entity 'slide' with mometum it as"""
        self.old_coords[0] = self.coords[0]
        self.coords[0] += int(self.momentum_x)
        self._hitbox_calculation()
        while True:
            tmp = self.collision(blocs, bool(self.momentum_y<0))
            if tmp[0]:
                break
            if tmp[1] == -1:
                return
            self.coords[0] = tmp[1].left -self.hitbox_dimension[0]
            self.momentum_x = 0
            self._hitbox_calculation()
        self.old_coords[0] = self.coords[0]
        self.coords[0] += int(self.momentum_x)
        self._hitbox_calculation()
        while True:
            tmp = self.collision(blocs, bool(self.momentum_y<0))
            if tmp[0]:
                break
            if tmp[1] == -1:
                return
            self.coords[0] = tmp[1].right
            self.momentum_x = 0
            self._hitbox_calculation()

    def passive(self, blocs : list[GameBaseBloc], clock : pygame.time.Clock) -> Literal[-1] | None:
        """
        all the 'passive' action of the entity
        like : loosing momentum, making him subjext to gravity
        """
        if (clock.get_time()%(StageVariable.wind_time+StageVariable.wind_cooldown)
            >= StageVariable.wind_cooldown):
            self.momentum_x += StageVariable.wind_strenght
        if self.momentum_x <= 1 and self.momentum_x >= -1:
            self.momentum_x = 0.0
        else:
            self.momentum_x -= math.copysign(self.loose_mometum_x, self.momentum_x)
        return super().base_passive(blocs)

    @abstractmethod
    def interaction(self, __o : 'GameBaseEntity'):
        """a method to handle interaction with other entity (collission)"""
        raise NotImplementedError

    def render(self, screen : pygame.surface.Surface) -> None:
        """render the entity on the screen"""
        screen.blit(self.sprites, self.coords)
