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
    def __init__(self, coords : Iterable) -> None:
        self._rect_hitbox : pygame.Rect
        self.hitbox : tuple[int, int]
        self.coords : list[int, int] = list(coords)
        self.old_coords : list[int, int] = list(coords)
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
    def hitbox_dimension(self, w_x: int, h_y : int) -> None:
        """
        redefine the hitbox
        W_x represent the width of the hitbox
        H_y represent the height of the hitbox
        note: the hitbox is always a rectengle
        """
        self.hitbox = (w_x, h_y)

    @property
    def rect_hitbox(self) -> pygame.Rect:
        """give the rect hitbox of the object"""
        return self._rect_hitbox

    @rect_hitbox.setter
    def rect_hitbox(self) -> None:
        self._rect_hitbox = pygame.Rect(self.coords[0], self.coords[1],
                                         self.hitbox[0], self.hitbox[1])

    def _hitbox_calculation(self) -> None:
        """claculate the hitbox of the object"""
        self._rect_hitbox = pygame.Rect(self.coords[0], self.coords[1],
                                         self.hitbox[0], self.hitbox[1])

    def on_floor(self, blocs : list) -> bool:
        """check if the object is on the 'floor'"""
        for b in blocs:
            if not b.tangible or self is b:
                continue
            if b.rect_hitbox.top == self.rect_hitbox.bottom -1:
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
        like : loosing momentum, making him subjext to gravity
        """
        self._gravity(blocs)
        if self.momentum_y != 0:
            self.has_jumped:bool(self.momentum_y<0 or self.has_jumped)
            self.old_coords[1] = self.coords[1]
            self.coords[1] += self.momentum_y
            self._hitbox_calculation()
            if self.momentum_y<0:
                while True:
                    tmp = self.collision(blocs,self.has_jumped)
                    if tmp[0]:
                        return None
                    if tmp[1] == -1:
                        return -1 #todo death
                    self.coords[1] = tmp[1].bottom+1
                    self.momentum_y = 0
        if self.momentum_y <= 1 and self.momentum_y >= -1:
            self.momentum_y = 0.0
        self._old_rect_hitbox = self._rect_hitbox
        self._hitbox_calculation()
        return None

    @abstractmethod
    def render(self, screen : pygame.surface.Surface) -> None:
        """render the object on the screen"""
        raise NotImplementedError

    def collision(self, blocs : list, is_jumping : bool
                ) -> tuple[Literal[False], pygame.Rect | Literal[-1]] | tuple[Literal[True], None]:
        """handle the collision of the entity with the blocs"""
        for b in blocs:
            if not b.tangible or (is_jumping and b.semisolid):
                continue
            if b.rect_hitbox.colliderect(self._rect_hitbox):
                if b.rect_hitbox.colliderect(self._old_rect_hitbox):
                    return False, -1 #death if entity
                return False, b.rect_hitbox
        return True, None

    @abstractmethod
    def animation(self):
        """a method to handle the animation of the entity"""
        raise NotImplementedError
