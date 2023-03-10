""" the base package for handeling the entity/blocs/physic of the game"""
import math
from typing import Iterable, Literal
from abc import ABC, abstractmethod
import pygame
from .entity_variable import EntityVariable
from .stage_variable import StageVariable

def better_controller_list()-> list["BetterController"]:
    """return a list of all the controllers connected to the computer"""
    pygame.joystick.init()
    tmp = []
    for i in range(pygame.joystick.get_count()):
        tmp.append(BetterController(pygame.joystick.Joystick(i)))
    return tmp


class BetterController():
    """a class made to handle controllers with pygame in a more simple way"""
    def __init__(self, controller : pygame.joystick.Joystick) -> None:
        self.control = controller
        self.name = controller.get_name()
        self.__has_hat = controller.get_numhats != 0
        match self.name:
            case "Wireless Gamepad":
                print("WARNING JOYCONS DO NOT WORK AS INTENDED !")
                print("WARNING JOYCONS JOYSTICK DO NOT WORK !")
                self.type = "NX_CONTROLLER"
            case "Nintendo Switch Pro Controller":
                self.type = "NX_PRO_CONTROLLER"
            case "Xbox 360 Controller":
                self.type = "X360_CONTROLLER"
            case "PS4 Controller":
                self.type = "PS4_CONTROLLER"
            case _:
                print("WARNING THIS CONTROLLER MAY NOT WORK AS INTENDED !")
                self.type = "UNRECONIZABLE"

    def is_pressed(self, button : int) -> bool:
        """return the current state of a button"""
        return self.control.get_button(button)

    def button_A_is_pressed(self) -> bool: #pylint: disable=invalid-name
        """
        return the current state of the A button
        note: cross button for PS4_CONTROLLER
                """
        return self.is_pressed(0)

    def button_B_is_pressed(self) -> bool: #pylint: disable=invalid-name
        """
        return the current state of the B button
        note: circle button for PS4_CONTROLLER
                """
        return self.is_pressed(1)

    def button_X_is_pressed(self) -> bool: #pylint: disable=invalid-name
        """
        return the current state of the X button
        note: square button for PS4_CONTROLLER
        not as be confused with cross buttton
        """
        return self.is_pressed(2)

    def button_Y_is_pressed(self) -> bool: #pylint: disable=invalid-name
        """
        return the current state of the Y button
        note: triangle button for PS4_CONTROLLER
        """
        return self.is_pressed(3)

    def left_bumber_is_pressed(self) -> bool:
        """
        return the current state of the left bumber
        SL on NX_CONTROLLER
        """
        match self.type:
            case "NX_CONTROLLER" | "X360_CONTROLLER":
                res = self.is_pressed(4)
            case "NX_PRO_CONTROLLER" | "PS4_CONTROLLER":
                res = self.is_pressed(9)
            case _:
                print("TRYING BUTTON 4")
                res = self.is_pressed(4)
        return res

    def right_bumber_is_pressed(self) -> bool:
        """
        return the current state of the left bumber
        SR on NX_CONTROLLER
        """
        match self.type:
            case "NX_CONTROLLER" | "X360_CONTROLLER":
                res = self.is_pressed(5)
            case "NX_PRO_CONTROLLER" | "PS4_CONTROLLER":
                res = self.is_pressed(10)
            case _:
                print("TRYING BUTTON 5")
                res = self.is_pressed(5)
        return res

    def back_button_is_pressed(self) -> bool:
        """
        return the current state of the back button
        note:
        Share button on PS4_CONTROLLER
        - button on NX_PRO_CONTROLLER
        not aviable with NX_CONTROLLER
        """
        match self.type:
            case "NX_CONTROLLER":
                print("not aviable")
                res = False
            case "X360_CONTROLLER":
                res = self.is_pressed(6)
            case "NX_PRO_CONTROLLER" | "PS4_CONTROLLER":
                res = self.is_pressed(4)
            case _:
                print("TRYING BUTTON 6")
                res = self.is_pressed(6)
        return res

    def start_button_is_pressed(self) -> bool:
        """
        return the current state of the start button
        note:
        option button on PS4-CONTROLLER
        + button on NX_PRO_CONTROLLER and NX_CONTROLLER
        """
        match self.type:
            case "NX_CONTROLLER":
                res = self.is_pressed(8)
            case "X360_CONTROLLER":
                res = self.is_pressed(7)
            case "NX_PRO_CONTROLLER" | "PS4_CONTROLLER":
                res = self.is_pressed(6)
            case _:
                print("TRYING BUTTON 7")
                res = self.is_pressed(7)
        return res

    def left_stick_is_pressed(self) -> bool:
        """
        return if the left joystick is pressed
        LS and RS are mixed on NX_CONTROLLER
        """
        match self.type:
            case "NX_CONTROLLER":
                res = self.is_pressed(11)
            case "X360_CONTROLLER":
                res = self.is_pressed(8)
            case "NX_PRO_CONTROLLER" | "PS4_CONTROLLER":
                res = self.is_pressed(7)
            case _:
                print("TRYING BUTTON 8")
                res = self.is_pressed(8)
        return res

    def right_stick_is_pressed(self) -> bool:
        """
        return if the left joystick is pressed
        LS and RS are mixed on NX_CONTROLLER
        """
        match self.type:
            case "NX_CONTROLLER":
                res = self.is_pressed(11)
            case "X360_CONTROLLER":
                res = self.is_pressed(9)
            case "NX_PRO_CONTROLLER" | "PS4_CONTROLLER":
                res = self.is_pressed(8)
            case _:
                print("TRYING BUTTON 9")
                res = self.is_pressed(9)
        return res

    def get_dpad(self) -> tuple[float, float]:
        """
        return a tuple with the current state of the d-pad
        [0] : left -> right
        [1] : up -> down
        """
        if self.__has_hat:
            res = self.control.get_hat(0)
            return -res[0], res[1]
        res: list[float, float] = [0.0, 0.0]
        match self.type:
            case "NX_CONTROLLER":
                if self.is_pressed(0):
                    res[1]-=1
                if self.is_pressed(1):
                    res[1]+=1
                if self.is_pressed(2):
                    res[0]-=1
                if self.is_pressed(3):
                    res[0]+=1

            case "PS4_CONTROLLER" | "NX_PRO_CONTROLLER":
                if self.is_pressed(11):
                    res[1]-=1
                if self.is_pressed(12):
                    res[1]+=1
                if self.is_pressed(13):
                    res[0]-=1
                if self.is_pressed(14):
                    res[0]+=1
            case _:
                print("NO HAT AVIABLE !")
        return tuple(res)

    def get_left_stick(self) -> tuple[float, float]:
        """
        return a tuple with the current state of the left stick
        [0] : left -> right
        [1] : up -> down
        """
        if self.type == "NX_CONTROLLER":
            return 0.0 , 0.0
        return self.control.get_axis(0), self.control.get_axis(1)

    def get_right_stick(self) -> tuple[float, float]:
        """
        return a tuple with the current state of the right stick
        [0] : left -> right
        [1] : up -> down
        """
        match self.type:
            case "NX_CONTROLLER":
                return 0.0 , 0.0
            case "X360_CONTROLLER":
                return self.control.get_axis(3), self.control.get_axis(4)
            case _:
                return self.control.get_axis(2), self.control.get_axis(3)

    def get_left_trigger(self) -> float:
        """
        return a float of the current state of the left trigger
        out -> in
        ZR and ZL are mixed on NX_CONTROLLER and are either 1.0 or 0.0
        """
        match self.type:
            case "NX_CONTROLLER":
                if self.is_pressed(15):
                    return 1.0
                return 0.0
            case "X360_CONTROLLER":
                return self.control.get_axis(2)
            case _:
                return self.control.get_axis(4)

    def get_right_trigger(self) -> float:
        """
        return a float of the current state of the right trigger
        out -> in
        ZR and ZL are mixed on NX_CONTROLLER and are either 1.0 or 0.0
        """
        match self.type:
            case "NX_CONTROLLER":
                if self.is_pressed(15):
                    return 1.0
                return 0.0
            case _:
                return self.control.get_axis(5)

    def get_name(self) -> str:
        """return the name of the controller"""
        return self.name

    def get_type(self) -> str:
        """return the type (brand) of the controller"""
        return self.type


class GameBaseObject(ABC):
    """
    base class for game object
    this class is abstract
    therfor you can never create an object with it !
    """
    def __init__(self, coords : Iterable) -> None:
        self.__rect_hitbox : pygame.Rect
        self.__hitbox : tuple[int, int]
        self.coords : list[int, int] = list(coords)
        self.old_coords : list[int, int] = list(coords)
        self.__hitbox_calculation()
        self.__old_rect_hitbox : pygame.Rect = self.__rect_hitbox
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
        return self.__hitbox

    @hitbox_dimension.setter
    def hitbox_dimension(self, w_x: int, h_y : int) -> None:
        """
        redefine the hitbox
        W_x represent the width of the hitbox
        H_y represent the height of the hitbox
        note: the hitbox is always a rectengle
        """
        self.__hitbox = (w_x, h_y)

    @property
    def rect_hitbox(self) -> pygame.Rect:
        """give the rect hitbox of the object"""
        return self.__rect_hitbox

    @rect_hitbox.setter
    def rect_hitbox(self) -> None:
        self.__rect_hitbox = pygame.Rect(self.coords[0], self.coords[1],
                                         self.__hitbox[0], self.__hitbox[1])

    def __hitbox_calculation(self) -> None:
        """claculate the hitbox of the object"""
        self.__rect_hitbox = pygame.Rect(self.coords[0], self.coords[1],
                                         self.__hitbox[0], self.__hitbox[1])

    def on_floor(self, blocs : list['GameBaseBloc']) -> bool:
        """check if the object is on the 'floor'"""
        for b in blocs:
            if not b.tangible or self is b:
                continue
            if b.rect_hitbox.top == self.rect_hitbox.bottom -1:
                self.has_jumped = False
                return True
        return False

    def __gravity(self, blocs: list['GameBaseBloc']) -> None:
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

    def passive(self, blocs: list['GameBaseBloc']) -> Literal[-1] | None:
        """
        all the 'passive' action of the object
        like : loosing momentum, making him subjext to gravity
        """
        self.__gravity(blocs)
        if self.momentum_y != 0:
            self.has_jumped:bool(self.momentum_y<0 or self.has_jumped)
            self.old_coords[1] = self.coords[1]
            self.coords[1] += self.momentum_y
            self.__hitbox_calculation()
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
        self.__old_rect_hitbox = self.__rect_hitbox
        self.__hitbox_calculation()
        return None

    @abstractmethod
    def render(self, screen : pygame.surface.Surface) -> None:
        """render the object on the screen"""
        raise NotImplementedError

    def collision(self, blocs : list['GameBaseBloc'], is_jumping : bool
                  ) -> tuple[Literal[False], pygame.Rect | -1] | tuple[Literal[True], None]:
        """handle the collision of the entity with the blocs"""
        for b in blocs:
            if not b.tangible or (is_jumping and b.semisolid):
                continue
            if b.rect_hitbox.colliderect(self.__rect_hitbox):
                if b.rect_hitbox.colliderect(self.__old_rect_hitbox):
                    return False, -1 #death if entity
                return False, b.rect_hitbox
        return True, None

    @abstractmethod
    def animation(self):
        """a method to handle the animation of the entity"""
        raise NotImplementedError

class GameBaseBloc(GameBaseObject, ABC):
    """
    base class for game bloc
    this class is abstract
    therfor you can never create an object with it !
    """
    def __init__(self, coords : Iterable) -> None:
        self.__semi_solid: bool
        self.__is_tangible : bool
        self.__is_subject_to_gravity : bool
        self.sprites : Iterable
        super().__init__(coords)

    @property
    def semisolid(self) -> bool:
        """if the bloc is a semi solid (you can go throught if you jump)"""
        return self.__semi_solid

    @property
    def tangible(self) -> bool:
        """return True if the object as collision"""
        return self.__is_tangible

    @property
    def gravity_mode(self) -> tuple[int, int]:
        """
        redefine the hitbox
        W_x represent the width of the hitbox
        H_y represent the height of the hitbox
        note: the hitbox is always a rectengle
        """
        return self.__is_subject_to_gravity

    @gravity_mode.setter
    def gravity_mode(self, arg : bool) -> None:
        """
        redefine the hitbox
        W_x represent the width of the hitbox
        H_y represent the height of the hitbox
        note: the hitbox is always a rectangle
        """
        self.__is_subject_to_gravity = arg

    def passive(self, blocs: list['GameBaseBloc']) -> None:
        """
        all the 'passive' action of the bloc
        like : loosing momentum, making him subjext to gravity
        """
        if not self.gravity_mode:
            return
        super().passive(blocs)

    def render(self, screen : pygame.surface.Surface) -> None:
        """render the entity on the screen"""
        screen.blit(self.sprites, self.coords)

class GameBaseEntity(GameBaseObject, EntityVariable, ABC):
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
                self.momentum_x = -self.initial_value_mometum_x
            elif self.momentum_x > -self.max_mometum_x:
                self.momentum_x -= self.increasse_mometum_x
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
                self.momentum_x = self.initial_value_mometum_x
            elif self.momentum_x < self.max_mometum_x:
                self.momentum_x +=self.increasse_mometum_x
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

    def passive(self, blocs : list[GameBaseBloc], clock : pygame.time.Clock) -> None:
        """
        all the 'passive' action of the entity
        like : loosing momentum, making him subjext to gravity
        """
        if (clock.get_time()%StageVariable.wind_time+StageVariable.wind_cooldown) <= StageVariable.wind_time:
            self.momentum_x += StageVariable.wind_strenght
        if self.momentum_x <= 1 and self.momentum_x >= -1:
            self.momentum_x = 0.0
        else:
            self.momentum_x -= math.copysign(self.loose_mometum_x, self.momentum_x)
        super().passive(blocs)

    @abstractmethod
    def interaction(self, __o : 'GameBaseEntity'):
        """a method to handle interaction with other entity (collission)"""
        raise NotImplementedError

    def render(self, screen : pygame.surface.Surface) -> None:
        """render the entity on the screen"""
        screen.blit(self.sprites, self.coords)

class Player(GameBaseEntity):
    """ a subclass of GameBaseEntity handeling a player"""
    def __init__(self, coords) -> None:
        sprites = pygame.surface.Surface((10,10))
        sprites.fill('red')
        self.sprites = sprites
        self.jump_lock=False
        self.gain_vector_y : float = 0.0
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


print('Hello from Noruaric !')
