"""this module contain the base class for any object of the game"""
from typing import Iterable, Literal
from abc import ABC, abstractmethod
import pygame
from .stage_variable import StageVariable

class GameBaseObject(ABC):
    """
    base class for game object
    this class is abstract
    therfor you can never create an object with it !
    """

    def __new__(cls, *args, **kwargs):
        if cls is GameBaseObject:
            raise TypeError("the abstarct class GameBaseObject can't be instancied.")
        return super().__new__(cls)

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
        self._dead = False
        self._rect_hitbox : pygame.Rect
        self.hitbox : tuple[int, int]
        self.coords : list[int] = list(coords)
        self.old_coords : list[int] = list(coords)
        self._hitbox_calculation()
        self._old_rect_hitbox : pygame.Rect = self._rect_hitbox
        self.momentum_y : float = 0.0
        self.has_jumped : bool = False

    @property
    def hitbox_dimension(self) -> tuple[int, int]:
        """
        redefine the hitbox
        W_x represent the width of the hitbox
        H_y represent the height of the hitbox
        note: the hitbox is always a rectengle
        """
        return self.hitbox

    @hitbox_dimension.setter
    def hitbox_dimension(self, dimension:Iterable[int]) -> None:
        """
        redefine the hitbox
        W_x represent the width of the hitbox
        H_y represent the height of the hitbox
        note: the hitbox is always a rectengle
        """
        if not isinstance(dimension, tuple) and not isinstance(dimension, tuple):
            raise TypeError(f'dimension should be Iterable object got {type(dimension)}')
        if i:=len(dimension):
            raise ValueError(f'dimension should have 2 element got {i}')
        if not isinstance(dimension[0], int) or not isinstance(dimension[1], int):
            raise TypeError(
                f'dimension should only conataint int object got \
                    {type(dimension[0])} and {type(dimension[1])}')
        if dimension[0] <= 0 or dimension[1] <= 0:
            raise TypeError(
                f'dimension should only conataint int object > 0 \
                    got {dimension[0]} and {dimension[1]}')
        self.hitbox =  tuple(dimension)

    @property
    def rect_hitbox(self) -> pygame.Rect:
        """give the rect hitbox of the object"""
        return self._rect_hitbox

    @property
    def is_dead(self):
        """return True if the object is dead (therfor should be ignored)"""
        return self._dead

    @is_dead.setter
    def is_dead(self, arg : bool):
        if not isinstance(arg, bool):
            raise TypeError(f'arg should be a boolean got {type(arg)}')
        self._dead = arg

    def _hitbox_calculation(self) -> None:
        """claculate the hitbox of the object"""
        self._rect_hitbox = pygame.Rect(self.coords[0], self.coords[1],
                                         self.hitbox[0], self.hitbox[1])

    def on_floor(self, blocs : list) -> bool:
        """check if the object is on the 'floor'"""
        for i in blocs:
            if not i.tangible or self is i:
                continue
            if i.rect_hitbox.top == self.rect_hitbox.bottom:
                self.has_jumped = False
                return True
        return False

    def _gravity(self, blocs: list) -> None:
        """
        make the entity subject to the effect of graviy
        making it 'fall" and gain vertical mometum
        (or loose if he jumped)
        """
        if not self.on_floor(blocs):
            if self.momentum_y == 0:
                self.momentum_y = 1.1 * StageVariable.gravity_strengh
            else:
                self.momentum_y += 0.25 * StageVariable.gravity_strengh
        elif self.momentum_y > 0:
            self.momentum_y = 0.0

    def base_passive(self, blocs: list) -> Literal[-1] | None:
        """
        all the 'passive' action of the object
        like : loosing momentum, making him subject to gravity
        """
        self._gravity(blocs)
        if self.momentum_y != 0:
            self.has_jumped=bool(self.momentum_y<0 or self.has_jumped)
            self.old_coords[1] = self.coords[1]
            self.coords[1] += self.momentum_y
            self._hitbox_calculation()
            if self.momentum_y<0:
                while True:
                    tmp = self.collision(blocs,self.has_jumped)
                    if tmp[0]:
                        return None
                    if tmp[1] == -1:
                        return self.death_seqeunce('crush')
                    self.coords[1] = tmp[1].bottom
                    self.momentum_y = 0
                    self._hitbox_calculation()
            if self.momentum_y>0:
                while True:
                    tmp = self.collision(blocs,self.has_jumped)
                    if tmp[0]:
                        return None
                    if tmp[1] == -1:
                        return self.death_seqeunce('crush')
                    self.coords[1] = tmp[1].top-self.hitbox_dimension[1]
                    self.momentum_y = 0
                    self._hitbox_calculation()
        if abs(self.momentum_y) <= 1:
            self.momentum_y = 0.0
        self._old_rect_hitbox = self._rect_hitbox
        self._hitbox_calculation()
        return None

    def collision(self, blocs : list, is_jumping : bool
                ) -> tuple[Literal[False], pygame.Rect | Literal[-1]] | tuple[Literal[True], None]:
        """handle the collision of the entity with the blocs"""
        if not isinstance(is_jumping, bool):
            raise TypeError(f'is_jumping should be a boolean got {type(is_jumping)}')
        for i in blocs:
            if not i.tangible or (is_jumping and i.semisolid) or i.is_dead:
                continue
            if i.rect_hitbox.colliderect(self._rect_hitbox):
                if i.rect_hitbox.colliderect(self._old_rect_hitbox):
                    return False, -1 #death if entity
                return False, i.rect_hitbox
        return True, None

    @abstractmethod
    def death_seqeunce(self, origin: str):
        """this function handle the death of a object"""
        raise NotImplementedError

    @abstractmethod
    def render(self, screen : pygame.surface.Surface, offset_x : int = 0, offset_y : int = 0) -> None:
        """render the object on the screen"""
        raise NotImplementedError

    @abstractmethod
    def animation(self):
        """a method to handle the animation of the entity"""
        raise NotImplementedError
