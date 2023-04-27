[Go Back][index]<br>

class GameBaseBloc(motoro.game_base_object.GameBaseObject, abc.ABC, builtins.object) <br>
   	GameBaseBloc(*args, **kwargs) <br>

base class for game bloc <br>
this class is abstract <br>
therfor you can never create an object with it ! <br>


	Method resolution order:


**GameBaseBloc** <br>
**motoro.game_base_object.GameBaseObject** <br>
**abc.ABC** <br>
**builtins.object** <br>


	Methods defined here:



**\_\_init\_\_(self, coords: Iterable[int])** -> None <br>
Initialize self.  See help(type(self)) for accurate signature. <br>
**death_seqeunce(self, origin: str)** <br>
this function handle the death of a object <br>
**passive(self, blocs: list['GameBaseBloc'])** -> Optional[Literal[-1]] <br>
all the 'passive' action of the bloc <br>
like : loosing momentum, making him subjext to gravity <br>
**render(self, screen: pygame.surface.Surface, offset_x: int = 0, offset_y: int = 0)** -> None <br>
render the bloc on the screen <br>
Static methods defined here: <br>
**\_\_new\_\_(cls, \*args, \*\*kwargs)** <br>
Create and return a new object.  See help(type) for accurate signature. <br>


	Readonly properties defined here:


**semisolid** <br>
if the bloc is a semi solid (you can go throught if you jump) <br>
**tangible** <br>
return True if the object as collision <br>


	Data descriptors defined here:


**gravity_mode** <br>
redefine the hitbox <br>
W_x represent the width of the hitbox <br>
H_y represent the height of the hitbox <br>
note: the hitbox is always a rectengle <br>


	Data and other attributes defined here:


### Methods inherited from motoro.game_base_object.GameBaseObject: <br>
**animation(self)** <br>
a method to handle the animation of the entity <br>
**base_passive(self, blocs: list)** -> Optional[Literal[-1]] <br>
all the 'passive' action of the object <br>
like : loosing momentum, making him subject to gravity <br>
**collision(self, blocs: list, is_jumping: bool)** -> tuple[typing.Literal[False], typing.Union[pygame.rect.Rect, typing.Literal <br>[-1]]] | tuple[typing.Literal[True], None] <br>
handle the collision of the entity with the blocs <br>
**on_floor(self, blocs: list)** -> bool <br>
check if the object is on the 'floor' <br>


### Readonly properties inherited from motoro.game_base_object.GameBaseObject: <br>
**rect_hitbox** <br>
give the rect hitbox of the object <br>

### Data descriptors inherited from motoro.game_base_object.GameBaseObject: <br>
**hitbox_dimension** <br>
redefine the hitbox <br>
W_x represent the width of the hitbox <br>
H_y represent the height of the hitbox <br>
note: the hitbox is always a rectengle <br>
**is_dead** <br>
return True if the object is dead (therfor should be ignored) <br>

[index]: ./index_EN.md