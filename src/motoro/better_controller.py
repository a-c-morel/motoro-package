import pygame

CONTROLLERS_TYPES_LIST = ["NX_CONTROLLER",
                          "NX_PRO_CONTROLLER",
                          "X360_CONTROLLER",
                          "PS4_CONTROLLER",
                          "UNRECONIZABLE"]

class BetterController():
    """a class made to handle controllers with pygame in a more simple way"""
    def __init__(self, controller : pygame.joystick.Joystick) -> None:
        self.control = controller
        self.__name = controller.get_name()
        self.__has_hat = controller.get_numhats != 0
        match self.__name:
            case "Wireless Gamepad":
                print("WARNING JOYCONS DO NOT WORK AS INTENDED !")
                print("WARNING JOYCONS JOYSTICK DO NOT WORK !")
                self.__type = "NX_CONTROLLER"
            case "Nintendo Switch Pro Controller":
                self.__type = "NX_PRO_CONTROLLER"
            case "Xbox 360 Controller":
                self.__type = "X360_CONTROLLER"
            case "PS4 Controller":
                self.__type = "PS4_CONTROLLER"
            case _:
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
        match self.__type:
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
        match self.__type:
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
        match self.__type:
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
        match self.__type:
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
        match self.__type:
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
        match self.__type:
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

    def get_dpad_status(self) -> tuple[float, float]:
        """
        return a tuple with the current state of the d-pad
        [0] : left -> right
        [1] : up -> down
        """
        if self.__has_hat:
            res = self.control.get_hat(0)
            return -res[0], res[1]
        res: list[float, float] = [0.0, 0.0]
        match self.__type:
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
        match self.__type:
            case "NX_CONTROLLER":
                return 0.0 , 0.0
            case "X360_CONTROLLER":
                return self.control.get_axis(3), self.control.get_axis(4)
            case _:
                return self.control.get_axis(2), self.control.get_axis(3)

    def get_left_trigger_status(self) -> float:
        """
        return a float of the current state of the left trigger
        out -> in
        ZR and ZL are mixed on NX_CONTROLLER and are either 1.0 or 0.0
        """
        match self.__type:
            case "NX_CONTROLLER":
                if self.is_pressed(15):
                    return 1.0
                return 0.0
            case "X360_CONTROLLER":
                return self.control.get_axis(2)
            case _:
                return self.control.get_axis(4)

    def get_right_trigger_status(self) -> float:
        """
        return a float of the current state of the right trigger
        out -> in
        ZR and ZL are mixed on NX_CONTROLLER and are either 1.0 or 0.0
        """
        match self.__type:
            case "NX_CONTROLLER":
                if self.is_pressed(15):
                    return 1.0
                return 0.0
            case _:
                return self.control.get_axis(5)

    @property
    def name(self) -> str:
        """return the name of the controller"""
        return self.__name

    @property
    def type(self) -> str:
        """return the type (brand) of the controller"""
        return self.__type
