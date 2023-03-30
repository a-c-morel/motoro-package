"""this module contain the base class for blocks aka not alive object"""
from typing import Iterable, Literal, Any
from abc import ABC
import pygame
from .game_base_object import GameBaseObject

class GameBaseBloc(GameBaseObject, ABC, object):
    """
    base class for game bloc
    this class is abstract
    therfor you can never create an object with it !
    """

    def __new__(cls, *args, **kwargs):
        if cls is GameBaseObject:
            raise TypeError("the abstarct class GameBaseObject can't be instancied.")
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
        self._semi_solid: bool
        self._is_tangible : bool
        self._is_subject_to_gravity : bool
        self.sprites : Iterable | Any
        self.current_frame : pygame.surface.Surface
        self.ignore_bloc_collision : bool
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
    def gravity_mode(self) -> bool:
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
        if not isinstance(arg, bool):
            raise TypeError(f'arg should be a boolean got {type(arg)}')
        self._is_subject_to_gravity = arg

    def death_seqeunce(self, origin: str):
        """this function handle the death of a object"""
        if not isinstance(origin, str):
            raise TypeError(f'origin should be a boolean got {type(origin)}')
        if origin == 'crush' and not self.ignore_bloc_collision:
            self.is_dead = True #pylint: disable=attribute-defined-outside-init
            return
        raise ValueError(f'unregonized death origin got {origin}')

    def passive(self, blocs: list['GameBaseBloc'])  -> Literal[-1] | None:
        """
        all the 'passive' action of the bloc
        like : loosing momentum, making him subjext to gravity
        """
        if not isinstance(blocs, list):
            raise TypeError(f'block should be a list object got {type(blocs)}')
        for i in blocs:
            if not isinstance(i, GameBaseBloc):
                raise TypeError(f'block should only contain GameBaseBloc instance got {type(i)}')
        if not self.gravity_mode:
            return None
        return super().base_passive(blocs)

    def render(self, screen: pygame.surface.Surface, offset_x: int = 0, offset_y: int = 0) -> None:
        """render the bloc on the screen"""
        if not isinstance(screen, pygame.surface.Surface):
            raise TypeError(f'screen should be a pygame.surface.Surface object got {type(screen)}')
        if not isinstance(offset_x, int):
            raise TypeError(f'offset_x should be a int object got {type(offset_x)}')
        if not isinstance(offset_y, int):
            raise TypeError(f'offset_x should be a int object got {type(offset_y)}')
        screen.blit(self.current_frame, (self.coords[0] + offset_x, self.coords[1] + offset_y))
