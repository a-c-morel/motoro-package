[Go Back][index]<br>

class BetterController(builtins.object) <br>
BetterController(controller: pygame.joystick.Joystick) -&gt; None

a class made to handle controllers with pygame in a more simple way

	Methods defined here:


**\_\_init\_\_(self, controller: pygame.joystick.Joystick) -> None** <br>
Initialize self.  <br>
See help(type(self)) for accurate signature.
<br><br>

**back_button_is_pressed(self) -> bool**<br>
return the current state of the back button<br>
note:<br>
Share button on PS4_CONTROLLER<br>
 \- button on NX_PRO_CONTROLLER<br>
not aviable with NX_CONTROLLER
<br><br>

**button_A_is_pressed(self) -> bool**<br>
return the current state of the A button<br>
note: cross button for PS4_CONTROLLER
<br><br>

**button_B_is_pressed(self) -> bool**<br>
return the current state of the B button<br>
note: circle button for PS4_CONTROLLER
<br><br>

**button_X_is_pressed(self) -> bool**<br>
return the current state of the X button<br>
note: square button for PS4_CONTROLLER<br>
not as be confused with cross buttton
<br><br>

**button_Y_is_pressed(self) -> bool**<br>
return the current state of the Y button<br>
note: triangle button for PS4_CONTROLLER
<br><br>

**get_dpad_status(self) -> list\[float\]**<br>
return a tuple with the current state of the d-pad<br>
[0] : left -> right<br>
[1] : up -> down<br><br>

**get_left_stick_status(self) -> tuple[float, float]**<br>
return a tuple with the current state of the left stick<br>
[0] : left -> right<br>
[1] : up -> down
<br><br>

**get_left_trigger_status(self) -> float**<br>
return a float of the current state of the left trigger<br>
out -> in<br>
ZR and ZL are mixed on NX_CONTROLLER and are either 1.0 or 0.0
<br><br>

**get_right_stick_status(self) -> tuple[float, float]**<br>
return a tuple with the current state of the right stick<br>
[0] : left -> right<br>
[1] : up -> down
<br><br>

**get_right_trigger_status(self) -> float**<br>
return a float of the current state of the right trigger<br>
out -> in<br>
ZR and ZL are mixed on NX_CONTROLLER and are either 1.0 or 0.0
<br><br>

**is_pressed(self, button_index: int) -> bool**<br>
return the current state of a button
<br><br>

**left_bumber_is_pressed(self) -> bool**<br>
return the current state of the left bumber<br>
SL on NX_CONTROLLER
<br><br>

**left_stick_is_pressed(self) -> bool**<br>
return if the left joystick is pressed<br>
LS and RS are mixed on NX_CONTROLLER
<br><br>
**right_bumber_is_pressed(self) -> bool**<br>
return the current state of the left bumber<br>
SR on NX_CONTROLLER
<br><br>
**right_stick_is_pressed(self) -> bool**<br>
return if the left joystick is pressed<br>
LS and RS are mixed on NX_CONTROLLER
<br><br>

**start_button_is_pressed(self) -> bool**<br>
return the current state of the start button<br>
note:<br>
option button on PS4-CONTROLLER<br>
\+ button on NX_PRO_CONTROLLER and NX_CONTROLLER<br>
Static methods defined here:
<br><br>

**get_better_controller_list() -> list\['BetterController'\]**<br>
return a list of all the controllers connected to the computer<br>

	Readonly properties defined here


name<br>
return the name of the controller<br><br>
type<br>
return the type (brand) of the controller<br>

	Data


CONTROLLERS_TYPES_LIST = ['NX_CONTROLLER', 'NX_PRO_CONTROLLER', 'X360_CONTROLLER', 'PS4_CONTROLLER', 'UNRECONIZABLE']

[index]: ./index_FR.md