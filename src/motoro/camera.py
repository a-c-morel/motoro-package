import random
import pygame
from .game_base_object import GameBaseObject

class camera:
    """create a camera object for the game"""
    def __init__(self, screen: pygame.Surface, anchor_object: None | GameBaseObject = None) -> None:
        if not isinstance(anchor_object, GameBaseObject):
            raise TypeError(f'anchor should be GameBaseObject subclass got {type(anchor_object)}')
        self.coord_x = 0
        self.coord_y = 0
        self.offset_x = 0
        self.offset_y = 0
        self.camera_shaking_time = 0 #in frame
        self._anchor = anchor_object
        self.display = screen

    def go_left(self, val : int):
        """make the camera go left (in pixel)"""
        if isinstance(val, int):
            raise TypeError(f"val should be a int got {type(val)}")
        self.coord_x -= val

    def go_right(self, val):
        """make the camera go right (in pixel)"""
        if isinstance(val, int):
            raise TypeError(f"val should be a int got {type(val)}")
        self.coord_x += val

    def go_up(self, val):
        """make the camera go up (in pixel)"""
        if isinstance(val, int):
            raise TypeError(f"val should be a int got {type(val)}")
        self.coord_y += val

    def go_down(self, val):
        """make the camera go down (in pixel)"""
        if isinstance(val, int):
            raise TypeError(f"val should be a int got {type(val)}")
        self.coord_y -= val

    def __didplay_blits(self, elements : list[GameBaseObject]):
        shx, shy =self.__camera_shaking()
        for i in elements:
            i.render(self.display, self.coord_x + shx, self.coord_y + shy)

    def display_update(self, elements : list[GameBaseObject]):
        """update the display by bliting elements"""
        if self.anchor is not None:
            self.coord_x = self.offset_x + self.anchor.coords[0]
            self.coord_y = self.offset_y + self.anchor.coords[1]
        self.__didplay_blits(elements)

    def __camera_shaking(self):
        if self.camera_shaking_time == 0:
            return 0, 0
        self.camera_shaking_time -= 1
        return random.randint(-5, 5), random.randint(-5, 5)

    @property
    def anchor(self):
        """define the anchor that the camera will follow (not mendatory)"""
        return self._anchor

    @anchor.setter
    def anchor(self, new_anchor : GameBaseObject):
        if not isinstance(new_anchor, GameBaseObject):
            raise TypeError(f'anchor should be GameBaseObject subclass got {type(new_anchor)}')
        self._anchor = new_anchor

    @anchor.deleter
    def anchor(self):
        self._anchor = None
