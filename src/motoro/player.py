"""contain the class to handle player"""
import pygame
from .game_base_entity import GameBaseEntity
from .game_base_bloc import GameBaseBloc

class Player(GameBaseEntity):
    """ a subclass of GameBaseEntity handeling a player"""
    def __init__(self, coords) -> None:
        sprites = pygame.surface.Surface((10,10))
        sprites.fill('red')
        self.sprites = sprites
        self.jump_lock=False
        self.gain_vector_y : float = 0.0

        super().__init__(coords)

    def jump(self, blocs : list[GameBaseBloc]) -> None:
        """make the player gain vertical mometum performing a jump"""
        if self.on_floor(blocs):
            self.jump_lock=False
        if self.momentum_y > 0 or self.jump_lock:
            return
        if self.momentum_y == 0.0:
            self.momentum_y = -1.36
            self.gain_vector_y = 0
        if self.gain_vector_y == 0:
            self.gain_vector_y = 1.125
        elif self.gain_vector_y > 1.5:
            self.jump_lock=True
        else:
            self.gain_vector_y += 0.125
        self.momentum_y *= self.gain_vector_y

    def animation(self):
        pass

    def interaction(self, __o: 'GameBaseEntity'):
        pass
