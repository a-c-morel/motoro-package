[Go Back][index]<br>
class GameRawEntity(motoro.game_base_object.GameBaseObject, abc.ABC)<br>
   	GameRawEntity(*args, **kwargs) <br>
 <br>
represent the proprety and base instance of an entity<br>


	Method resolution order:


**GameRawEntity**<br>
**motoro.game_base_object.GameBaseObject**<br>
**abc.ABC**<br>
**builtins.object**<br>


	Methods defined here:


**\_\_init\_\_**(self, coord, max_mometum_x: float = 4.0, initial_value_mometum_x: float = 1.1, increasse_mometum_x: float = 0.5, loose_mometum_x: float = 0.25, initial_jump_mometum: float = 1.36, initial_jump_gain: float = 1.125, <br>increase_jump_gain: float = 0.125, max_jump_gain: float = 1.5) -> None<br>
Initialize self.  See help(type(self)) for accurate signature.<br>
Static methods defined here:<br>
**\_\_new\_\_**(cls, *args, **kwargs)<br>
Create and return a new object.  See help(type) for accurate signature.<br>


	Data descriptors defined here:


**increase_jump_gain**<br>
proprety of the increase gain jump mometum<br>
**increasse_mometum_x**<br>
proprety of the increasse mometum x<br>
**initial_jump_gain**<br>
proprety of the gain jump mometum<br>
**initial_jump_mometum**<br>
proprety of the initial jump mometum<br>
**initial_value_mometum_x**<br>
proprety of the initial mometum x<br>
**loose_mometum_x**<br>
proprety of the loose mometum x<br>
**max_jump_gain**<br>
proprety of the max gain jump mometum<br>
**max_mometum_x**<br>
proprety of the max mometum x<br>


	Data and other attributes defined here:


\_\_abstractmethods\_\_ = frozenset({'animation', 'death_seqeunce', 'render'})<br>


	Methods inherited from motoro.game_base_object.GameBaseObject:


**animation(self)**<br>
a method to handle the animation of the entity<br>
**base_passive(self, blocs: list)** -> Optional[Literal[-1]]<br>
all the 'passive' action of the object<br>
like : loosing momentum, making him subject to gravity<br>
**collision(self, blocs: list, is_jumping: bool)** -> tuple[typing.Literal[False], typing.Union[pygame.rect.Rect, typing.Literal[-1]]] | tuple[typing.Literal[True], None]<br>
handle the collision of the entity with the blocs<br>
**death_seqeunce(self, origin: str)**<br>
this function handle the death of a object<br>
**on_floor(self, blocs: list)** -> bool<br>
check if the object is on the 'floor'<br>
**render(self, screen: pygame.surface.Surface, offset_x: int = 0, offset_y: int = 0)** -> None<br>
render the object on the screen<br>


	Readonly properties inherited from motoro.game_base_object.GameBaseObject:


**rect_hitbox**<br>
give the rect hitbox of the object<br>


	Data descriptors inherited from motoro.game_base_object.GameBaseObject:


**hitbox_dimension**<br>
redefine the hitbox<br>
W_x represent the width of the hitbox<br>
H_y represent the height of the hitbox<br>
note: the hitbox is always a rectengle<br>
**is_dead**<br>
return True if the object is dead (therfor should be ignored)<br>

[index]: ./index_EN.md