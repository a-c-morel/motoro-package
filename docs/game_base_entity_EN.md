[Go Back][index]<br>

class GameBaseEntity(motoro.game_raw_entity.GameRawEntity, abc.ABC)<br>
   	GameBaseEntity(*args, **kwargs)<br>
 <br>
base class for game entity<br>
this class is abstract<br>
therfor you can never create an object with it !<br>


	Method resolution order:


**GameBaseEntity**<br>
**motoro.game_raw_entity.GameRawEntity**<br>
**motoro.game_base_object.GameBaseObject**<br>
**abc.ABC**<br>
**builtins.object**<br>


	Methods defined here:<br>


**\_\_init\_\_(self, coords: Iterable[int])** -> None<br>
Initialize self.  See help(type(self)) for accurate signature.<br>
**death_seqeunce(self, origin: str)**<br>
this function handle the death of a entity<br>
**go_left(self, blocs: list[motoro.game_base_bloc.GameBaseBloc])** -> None<br>
make the entity go left and gain mometum<br>
**go_right(self, blocs) -> None**<br>
make the entity go right and gain mometum<br>
**interaction(self, _GameBaseEntity__o: 'GameBaseEntity')**<br>
a method to handle interaction with other entity (collission)<br>
**passive(self, blocs: list[motoro.game_base_bloc.GameBaseBloc], clock: pygame.time.Clock**) -> Optional\[Literal[-1]]<br>
all the 'passive' action of the entity<br>
like : loosing momentum, making him subjext to gravity<br>
**render(self, screen: pygame.surface.Surface, offset_x: int = 0, offset_y: int = 0)** -> None<br>
render the entity on the screen<br>
**sliding(self, blocs)** -> None<br>
make the entity 'slide' with mometum it as<br>


	Static methods defined here:


\_\_new\_\_(cls, *args, **kwargs)<br>
Create and return a new object.  See help(type) for accurate signature.<br>
Data and other attributes defined here:<br>
\_\_abstractmethods\_\_ = frozenset({'animation', 'death_seqeunce', 'interaction'})<br>
\_\_annotations\_\_ = {}<br>

	Data descriptors inherited from motoro.game_raw_entity.GameRawEntity:<br>

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


	Methods inherited from motoro.game_base_object.GameBaseObject:


**animation(self)**<br>
a method to handle the animation of the entity<br>
**base_passive(self, blocs: list)** -> Optional[Literal[-1]]<br>
all the 'passive' action of the object<br>
like : loosing momentum, making him subject to gravity<br>
**collision(self, blocs: list, is_jumping: bool)** -> tuple[typing.Literal[False], typing.Union[pygame.rect.Rect, typing.Literal<br>[-1]]] | tuple[typing.Literal[True], None]<br>
handle the collision of the entity with the blocs<br>
**on_floor(self, blocs: list)** -> bool<br>
check if the object is on the 'floor'<br>


	Readonly properties inherited from motoro.game_base_object.GameBaseObject:


**rect_hitbox**<br>
give the rect hitbox of the object<br>


	Data descriptors inherited from motoro.game_base_object.GameBaseObject:<br>


**hitbox_dimension**<br>
redefine the hitbox<br>
W_x represent the width of the hitbox<br>
H_y represent the height of the hitbox<br>
note: the hitbox is always a rectengle<br>
**is_dead**<br>
return True if the object is dead (therfor should be ignored)<br>

[index]: ./index_EN.md