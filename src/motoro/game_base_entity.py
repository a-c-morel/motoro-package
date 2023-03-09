"""contain the base class to handle entity"""
import math
from typing import Iterable
from abc import ABC, abstractmethod
import pygame
from .game_base_object import GameBaseObject
from .game_base_bloc import GameBaseBloc


class GameBaseEntity(GameBaseObject, ABC):
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
        if self.coords[0] > 0:
            self.old_coords[0] = self.coords[0]
            if self.momentum_x == 0:
                self.momentum_x = -1.1
            elif self.momentum_x > -4:
                self.momentum_x -= 0.5
            self.coords[0] += int(self.momentum_x)
            if self.coords[0] < 0:
                self.coords[0] = 0
                self.momentum_x = 0
            self.__hitbox_calculation()
            while True:
                tmp = self.collision(blocs, bool(self.momentum_y<0))
                if tmp[0]:
                    return
                self.coords[0] = tmp[1].right+1
                self.momentum_x = 0

    def go_right(self, blocs) -> None:
        """make the entity go right and gain mometum"""
        if self.coords[0] < 500:
            if self.momentum_x == 0:
                self.momentum_x = 1.1
            elif self.momentum_x < 4:
                self.momentum_x +=0.5
            self.coords[0] += int(self.momentum_x)
            if self.coords[0] > 500:
                self.coords[0] = 500
                self.momentum_x = 0
            self.__hitbox_calculation()
            while True:
                tmp = self.collision(blocs, bool(self.momentum_y<0))
                if tmp[0]:
                    return
                self.coords[0] = tmp[1].left - self.hitbox_dimension[0]-1
                self.momentum_x = 0

    def sliding(self, blocs) -> None:
        """make the entity 'slide' with mometum it as"""
        if self.coords[0] < 500:
            self.old_coords[0] = self.coords[0]
            self.coords[0] += int(self.momentum_x)
            self.__hitbox_calculation()
            while True:
                tmp = self.collision(blocs, bool(self.momentum_y<0))
                if tmp[0]:
                    return
                self.coords[0] = tmp[1].left -self.hitbox_dimension[0]-1
                self.momentum_x = 0
        if self.coords[0] > 0:
            self.old_coords[0] = self.coords[0]
            self.coords[0] += int(self.momentum_x)
            self.__hitbox_calculation()
            while True:
                tmp = self.collision(blocs, bool(self.momentum_y<0))
                if tmp[0]:
                    return
                self.coords[0] = tmp[1].right+1
                self.momentum_x = 0
        if self.coords[0] < 0:
            self.coords[0] = 0
            self.momentum_x = 0
        if self.coords[0] > 500:
            self.coords[0] = 500
            self.momentum_x = 0

    def passive(self, blocs : list[GameBaseBloc]) -> None:
        """
        all the 'passive' action of the entity
        like : loosing momentum, making him subjext to gravity
        """

        if self.momentum_x <= 1 and self.momentum_x >= -1:
            self.momentum_x = 0.0
        else:
            self.momentum_x -= math.copysign(0.25, self.momentum_x)
        super().passive(blocs)

    @abstractmethod
    def interaction(self, __o : 'GameBaseEntity'):
        """a method to handle interaction with other entity (collission)"""
        raise NotImplementedError

    def render(self, screen : pygame.surface.Surface) -> None:
        """render the entity on the screen"""
        screen.blit(self.sprites, self.coords)
