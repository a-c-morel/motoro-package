[Go Back][index] <br>
class camera(builtins.object)
   	camera(screen: pygame.surface.Surface, anchor_object: None | motoro.game_base_object.GameBaseObject = None) -&gt; None


create a camera object for the game


 	Methods defined here:
__init__(self, screen: pygame.surface.Surface, anchor_object: None | motoro.game_base_object.GameBaseObject = None) -> None<br>
Initialize self.
See help(type(self)) for accurate signature. <br>
**display_update**(self, elements: list[motoro.game_base_object.GameBaseObject]) <br>
update the display by bliting elements <br>
**go_down(self, val)** <br>
make the camera go down (in pixel) <br>
**go_left(self, val: int)** <br>
make the camera go left (in pixel) <br>
**go_right(self, val)** <br>
make the camera go right (in pixel) <br>
**go_up(self, val)** <br>
make the camera go up (in pixel) <br>

	Data descriptors defined here:
**anchor** <br>
define the anchor that the camera will follow (not mendatory) <br>

[index]: ./index_EN.md