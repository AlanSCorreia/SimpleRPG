import dataclasses


@dataclasses.dataclass(slots=True)
class Point:
	__current_value: int
	MAX_VALUE: int

	@property
	def current_value(
		self
	) -> int:
		
		return self.__current_value

	@current_value.setter
	def current_value(
		self,
		new_value: int
	) -> None:

		min_value: int = 0
		self.__current_value = min(self.MAX_VALUE, max(min_value, new_value))


@dataclasses.dataclass(slots=True)
class AttributePoints:
	strength	: Point
	resistence	: Point
	agility		: Point
	intelligence: Point


@dataclasses.dataclass(slots=True)
class StatisticPoints:
	health : Point
	stamina: Point
	spirit : Point
