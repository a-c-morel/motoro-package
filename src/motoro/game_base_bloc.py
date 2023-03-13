from typing import Iterable, Literal
from abc import ABC
import pygame
from .game_base_object import GameBaseObject

class GameBaseBloc(GameBaseObject, ABC):
    """
    base class for game bloc
    this class is abstract
    therfor you can never create an object with it !
    """
    def __init__(self, coords : Iterable) -> None:
        self._semi_solid: bool
        self._is_tangible : bool
        self._is_subject_to_gravity : bool
        self.sprites : Iterable
        super().__init__(coords)

    @property
    def semisolid(self) -> bool:
        """if the bloc is a semi solid (you can go throught if you jump)"""
        return self._semi_solid

    @property
    def tangible(self) -> bool:
        """return True if the object as collision"""
        return self._is_tangible

    @property
    def gravity_mode(self) -> tuple[int, int]:
        """
        redefine the hitbox
        W_x represent the width of the hitbox
        H_y represent the height of the hitbox
        note: the hitbox is always a rectengle
        """
        return self._is_subject_to_gravity

    @gravity_mode.setter
    def gravity_mode(self, arg : bool) -> None:
        """
        redefine the hitbox
        W_x represent the width of the hitbox
        H_y represent the height of the hitbox
        note: the hitbox is always a rectangle
        """
        self._is_subject_to_gravity = arg

    def passive(self, blocs: list['GameBaseBloc'])  -> Literal[-1] | None:
        """
        all the 'passive' action of the bloc
        like : loosing momentum, making him subjext to gravity
        """
        if not self.gravity_mode:
            return
        return super().base_passive(blocs)

    def render(self, screen : pygame.surface.Surface) -> None:
        """render the entity on the screen"""
        screen.blit(self.sprites, self.coords)
