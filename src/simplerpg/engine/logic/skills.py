import dataclasses
import enum


class SkillType(enum.Enum):
	PHYSICAL  = enum.auto()
	SPIRITUAL = enum.auto()


class SkillElement(enum.Enum):
	NONE  = enum.auto()
	WATER = enum.auto()
	EARTH = enum.auto()
	FIRE  = enum.auto()
	WIND  = enum.auto()


# TODO: Skills has their won levels, which means that they get stronger as their level raises
# 	- Using an skill successufuly gives experience points to it's user

#	- Not only the skill level influences the power of it, the level of your element also does
#		- Higher levels of your character element of choice enables to learn new skills and increases
#		  the mastery of that skill demanding less and giving more.
# 		  For example, A fireball with level 0 of affinity demands a lot for its user, but returns near nothing.
#		  Now, a user that level up the skill to the max and have a great mastery of its element not only
#		  has the greatest damage possible on that skill, it's also demands less and less resources from it's user

# The main idea it's a game where the player truly has to train it's character

@dataclasses.dataclass
class Skill:
	type_of: SkillType
	element: SkillElement

	MAX_USAGE_POINTS: int
	current_usage_points: int  # UP
	energy_consumption_points: int

	power_points: int  # PP
	amount_experience_per_use: float
