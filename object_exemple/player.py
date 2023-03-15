""" the base package for handeling the entity/blocs/physic of the game"""
import pygame
from motoro import GameBaseEntity, GameBaseBloc

class Player(GameBaseEntity):
    """a subclass of GameBaseEntity handeling a player"""
    def __init__(self, coords, hitbox_dimension) -> None:
        sprites = pygame.surface.Surface((10,10))
        sprites.fill('red')
        self.sprites = sprites
        self.jump_lock=False
        self.gain_vector_y : float = 0.0
        self.hitbox = hitbox_dimension #pylint: disable=unused-private-member
        super().__init__(coords)
        super().__init_subclass__()

    def jump(self, blocs : list[GameBaseBloc]) -> None:
        """make the player gain vertical mometum performing a jump"""
        if self.on_floor(blocs):
            self.jump_lock=False
        if self.momentum_y > 0 or self.jump_lock:
            return
        if self.momentum_y == 0.0:
            self.momentum_y = -self.initial_jump_mometum
            self.gain_vector_y = 0
        if self.gain_vector_y == 0:
            self.gain_vector_y = self.initial_jump_gain
        elif self.gain_vector_y > self.max_jump_gain:
            self.jump_lock=True
        else:
            self.gain_vector_y += self.increase_jump_gain
        self.momentum_y *= self.gain_vector_y

    def animation(self):
        pass

    def interaction(self, __o: 'GameBaseEntity'):
        pass
