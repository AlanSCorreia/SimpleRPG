import enum
import dataclasses

from simplerpg.engine.logic import points


class EntityTag(enum.Enum):
	PLAYER = enum.auto()
	ENEMY  = enum.auto()
	ALLY   = enum.auto()


class PlayerCurrentAction(enum.Enum):
	FIGHTING 	= enum.auto()
	EXPLORING 	= enum.auto()
	INTERACTING = enum.auto()


class EntityState(enum.Enum):
	ALIVE = enum.auto()
	DEAD  = enum.auto()


class Entity:
	def __init__(
		self,
		tag: EntityTag,
		name: str,
		statistic_points: points.StatisticPoints,
		attribute_points: points.AttributePoints
	) -> None:

		self.tag	: EntityTag	  = tag
		self.name	: str		  = name
		self.__state: EntityState = EntityState.ALIVE

		self.statistic_points: points.StatisticPoints = statistic_points
		self.attribute_points: points.AttributePoints = attribute_points
	
	@property
	def state(
		self
	) -> EntityState:

		return self.__state

	@state.setter
	def state(
		self,
		new_state: EntityState
	) -> None:
		
		self.__state = new_state
