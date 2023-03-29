"""
this module contain the class for better controller
which help to handle pygame.joystick.Joystick object
"""
import pygame

CONTROLLERS_TYPES_LIST = ["NX_CONTROLLER",
                          "NX_PRO_CONTROLLER",
                          "X360_CONTROLLER",
                          "PS4_CONTROLLER",
                          "UNRECONIZABLE"]

class BetterController():
    """a class made to handle controllers with pygame in a more simple way"""
    def __init__(self, controller : pygame.joystick.JoystickType) -> None:
        if not isinstance(controller, pygame.joystick.JoystickType):
            raise TypeError(f'controller should be JoystickType object got {type(controller)}')
        self.control = controller
        self.__name = controller.get_name()
        self.__has_hat = controller.get_numhats != 0
        if self.__name == "Wireless Gamepad":
            print("WARNING JOYCONS DO NOT WORK AS INTENDED !")
            print("WARNING JOYCONS JOYSTICK DO NOT WORK !")
            self.__type = "NX_CONTROLLER"
        elif self.__name == "Nintendo Switch Pro Controller":
            self.__type = "NX_PRO_CONTROLLER"
        elif self.__name == "Xbox 360 Controller":
            self.__type = "X360_CONTROLLER"
        elif self.__name == "PS4 Controller":
            self.__type = "PS4_CONTROLLER"
        else:
            print("WARNING THIS CONTROLLER MAY NOT WORK AS INTENDED !")
            self.__type = "UNRECONIZABLE"


    @staticmethod
    def get_better_controller_list()-> list["BetterController"]:
        """return a list of all the controllers connected to the computer"""
        pygame.joystick.init()
        tmp = []
        for i in range(pygame.joystick.get_count()):
            tmp.append(BetterController(pygame.joystick.Joystick(i)))
        return tmp

    def is_pressed(self, button_index : int) -> bool:
        """return the current state of a button"""
        if not isinstance(button_index, int):
            raise TypeError(f'button should be a int object got {type(button_index)}')
        if (num_buttons := self.control.get_numbuttons()) > button_index or button_index < 0:
            raise TypeError(
                f'button should be > 0 and < {num_buttons} got {button_index}')
        return self.control.get_button(button_index)

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
        if self.__type in ["NX_CONTROLLER", "X360_CONTROLLER"]:
            return self.is_pressed(4)
        if self.__type in ["NX_PRO_CONTROLLER", "PS4_CONTROLLER"]:
            return self.is_pressed(9)
        print("TRYING BUTTON 4")
        return self.is_pressed(4)


    def right_bumber_is_pressed(self) -> bool:
        """
        return the current state of the left bumber
        SR on NX_CONTROLLER
        """
        if self.__type in ["NX_CONTROLLER", "X360_CONTROLLER"]:
            return self.is_pressed(4)
        if self.__type == ["NX_PRO_CONTROLLER", "PS4_CONTROLLER"]:
            return self.is_pressed(9)
        print("TRYING BUTTON 4")
        return self.is_pressed(4)


    def back_button_is_pressed(self) -> bool:
        """
        return the current state of the back button
        note:
        Share button on PS4_CONTROLLER
        - button on NX_PRO_CONTROLLER
        not aviable with NX_CONTROLLER
        """
        if self.__type == "NX_CONTROLLER":
            print("not available")
            return False
        if self.__type == "X360_CONTROLLER":
            return self.is_pressed(6)
        if self.__type in ["NX_PRO_CONTROLLER", "PS4_CONTROLLER"]:
            return self.is_pressed(4)
        print("TRYING BUTTON 6")
        return self.is_pressed(6)

    def start_button_is_pressed(self) -> bool:
        """
        return the current state of the start button
        note:
        option button on PS4-CONTROLLER
        + button on NX_PRO_CONTROLLER and NX_CONTROLLER
        """
        if self.__type == "NX_CONTROLLER":
            return self.is_pressed(8)
        if self.__type == "X360_CONTROLLER":
            return self.is_pressed(7)
        if self.__type in ["NX_PRO_CONTROLLER", "PS4_CONTROLLER"]:
            return self.is_pressed(6)
        print("TRYING BUTTON 7")
        return self.is_pressed(7)


    def left_stick_is_pressed(self) -> bool:
        """
        return if the left joystick is pressed
        LS and RS are mixed on NX_CONTROLLER
        """
        if self.__type == "NX_CONTROLLER":
            return self.is_pressed(11)
        if self.__type == "X360_CONTROLLER":
            return self.is_pressed(8)
        if self.__type in ["NX_PRO_CONTROLLER", "PS4_CONTROLLER"]:
            return self.is_pressed(7)
        print("TRYING BUTTON 8")
        return self.is_pressed(8)


    def right_stick_is_pressed(self) -> bool:
        """
        return if the left joystick is pressed
        LS and RS are mixed on NX_CONTROLLER
        """
        if self.__type in ["NX_PRO_CONTROLLER", "PS4_CONTROLLER"]:
            return self.is_pressed(8)
        if self.__type == "NX_CONTROLLER":
            return self.is_pressed(11)
        if self.__type == "X360_CONTROLLER":
            return self.is_pressed(9)
        print("TRYING BUTTON 9")
        return self.is_pressed(9)

    def get_dpad_status(self) -> list[float]:
        """
        return a tuple with the current state of the d-pad
        [0] : left -> right
        [1] : up -> down
        """
        if self.__has_hat:
            res = list(self.control.get_hat(0))
            return [-res[0], res[1]]
        res: list[float] = [0.0, 0.0]
        if self.__type == "NX_CONTROLLER":
            up_button = 0
            down_button = 1
            left_button = 2
            right_button = 3
        elif self.__type in ["PS4_CONTROLLER", "NX_PRO_CONTROLLER"]:
            up_button = 11
            down_button = 12
            left_button = 13
            right_button = 14
        else:
            print("NO HAT AVAILABLE !")
            return res
        if self.is_pressed(up_button):
            res[1]-=1
        if self.is_pressed(down_button):
            res[1]+=1
        if self.is_pressed(left_button):
            res[0]-=1
        if self.is_pressed(right_button):
            res[0]+=1
        return res

    def get_left_stick_status(self) -> tuple[float, float]:
        """
        return a tuple with the current state of the left stick
        [0] : left -> right
        [1] : up -> down
        """
        if self.__type == "NX_CONTROLLER":
            return 0.0 , 0.0
        return self.control.get_axis(0), self.control.get_axis(1)

    def get_right_stick_status(self) -> tuple[float, float]:
        """
        return a tuple with the current state of the right stick
        [0] : left -> right
        [1] : up -> down
        """
        if self.__type == "NX_CONTROLLER":
            return 0.0, 0.0
        if self.__type == "X360_CONTROLLER":
            return self.control.get_axis(3), self.control.get_axis(4)
        return self.control.get_axis(2), self.control.get_axis(3)


    def get_left_trigger_status(self) -> float:
        """
        return a float of the current state of the left trigger
        out -> in
        ZR and ZL are mixed on NX_CONTROLLER and are either 1.0 or 0.0
        """
        if self.__type == "NX_CONTROLLER":
            if self.is_pressed(15):
                return 1.0
            return 0.0
        if self.__type == "X360_CONTROLLER":
            return self.control.get_axis(2)
        return self.control.get_axis(4)


    def get_right_trigger_status(self) -> float:
        """
        return a float of the current state of the right trigger
        out -> in
        ZR and ZL are mixed on NX_CONTROLLER and are either 1.0 or 0.0
        """
        if self.__type == "NX_CONTROLLER":
            if self.is_pressed(15):
                return 1.0
            return 0.0
        return self.control.get_axis(5)


    @property
    def name(self) -> str:
        """return the name of the controller"""
        return self.__name

    @property
    def type(self) -> str:
        """return the type (brand) of the controller"""
        return self.__type
