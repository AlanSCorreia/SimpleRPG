from dataclasses import dataclass
from time import sleep
from subprocess import call
from enum import Enum, auto
from random import choice

import yaml


with open("./data/teste.yaml", "r") as file:
	print(yaml.safe_load(file))


class EAttack(Enum):
	PHYSICAL  = auto()
	SPIRITUAL = auto()


class EStatistic(Enum):
	HEALTH  = auto()
	SPIRIT  = auto()
	STAMINA = auto()


@dataclass(slots=True)
class PhysicalAttributes:
	strength:   int
	resistence: int


@dataclass(slots=True)
class SpiritualAttributes:
	strength:   int
	resistence: int


@dataclass(slots=True)
class StatisticPoint:
	__current_value: int
	max_value: int

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

		self.__current_value = min(self.max_value, max(0, new_value))


class Entity:
	def __init__(
		self,
		name: str,
		statistics: dict[EStatistic, StatisticPoint],
		attributes: dict[EAttack, PhysicalAttributes | SpiritualAttributes]
	) -> None:

		self.name: str = name
		self.statistics: dict[EStatistic, StatisticPoint] = statistics
		self.attributes: dict[EAttack, PhysicalAttributes | SpiritualAttributes] = attributes


class BattleSystem:
	def __init__(
		self,
		entity_1: Entity,
		entity_2: Entity
	) -> None:

		self.entity_1: Entity = entity_1
		self.entity_2: Entity = entity_2

		self.__entity_attacker: Entity = self.entity_1
		self.__entity_defender: Entity = self.entity_2
	
	def __change_turns(
		self
	) -> None:

		# Changes the roles of the entities in the actual turn of the battle
		value_holder: Entity = self.__entity_attacker
		self.__entity_attacker = self.__entity_defender
		self.__entity_defender = value_holder
	
	def __calculate_damage(
		self,
		attack_type: EAttack
	) -> int:

		# Calculate how much damage an entity causes to the other
		return self.__entity_attacker.attributes[attack_type].strength\
			   *(100/(100+self.__entity_defender.attributes[attack_type].resistence))
	
	def __try_to_flee(
		self
	) -> bool:

		has_flee_succeded: bool = choice([True, False])
		return has_flee_succeded
	
	def __menu_attack_types(
		self
	) -> bool:

		# TODO: Muitas responsabilidades em um só metodo, acho que preciso dizer mais nada
		attack_type: EAttack | None = None

		question = int(self.__validated_input(
			"Types of attack available:\n"\
			+"1) Physical\n"\
			+"2) Spiritual\n"\
			+"Which type of attack do you want to use: ",	
			"Enter a valid input [ 1 / 2 ]: ",
			lambda x: x.isdigit() and int(x) in (1, 2)
		))

		match question:
			case 1: attack_type = EAttack.PHYSICAL
			case 2: attack_type = EAttack.SPIRITUAL
		
		self.__entity_defender.statistics[EStatistic.HEALTH].current_value -= self.__calculate_damage(attack_type)

		return self.__entity_defender.statistics[EStatistic.HEALTH].current_value > 0
	
	def __menu_items(
		self	
	) -> str:
		
		result: str = "Necessita mais desenvolvimento"

		return result
	
	def __validated_input(
		self,
		input_question_1: str,
		input_question_2: str,
		valid_condition: bool
	) -> str:

		is_in_verification: bool = True
		new_input: str = input(input_question_1).strip()

		while is_in_verification:

			if valid_condition(new_input):
				is_in_verification = False
				continue
			
			new_input = input(input_question_2).strip()
		
		return new_input

	
	def __switch_options(
		self,
		option: int
	) -> bool:

		# TODO: Muitas responsabilidades juntas, pensar em uma melhor solução/arquitetura
		match option:
			case 1:
				return self.__menu_attack_types()

			# TODO: Assim que implementar Itens, refatorar este use case para tratar dados apropriadamente
			case 2:
				print(self.__menu_items())
				sleep(1.5)
				return True
				
			case default:
				if self.__try_to_flee():
					print("You fled the fight")
					sleep(2)
					return False
				else:
					print("You can't flee the fight")
					sleep(2)
					return True
		
	def start(
		self
	) -> None:

		is_battle_happening: bool = True
		input_question_1: str = "Available actions:\n"\
			+"1)Attack the other entity\n"\
			+"2)Use an item\n"\
			+"3)Try to flee\n"\
			+"Which action do you choose? "
		input_question_2: str = "Enter a valid input [ 1 / 2 / 3 ]: "

		call("clear")

		# Loop where the battle happens
		while is_battle_happening:
			for entity in (self.entity_1, self.entity_2):
				print(
					f"name: {entity.name}\n"
					+f"HP: {entity.statistics[EStatistic.HEALTH].current_value}\n"
					+f"SP: {entity.statistics[EStatistic.SPIRIT].current_value}"
				)

			# Ask to the attacker what he will do
			attackers_choice: int = int(self.__validated_input(
				input_question_1,
				input_question_2,
				lambda x: x.isdigit() and int(x) in range(1, 4)
			))
			
			# Execute his input
			is_battle_happening = self.__switch_options(attackers_choice)

			# Changes the role of the entities
			self.__change_turns()
			call("clear")
		
		print("The battle has ended.")


if __name__ == "__main__":

	entity_A: Entity = Entity(
		"A",
		{
			EStatistic.HEALTH: StatisticPoint(20, 100),
		 	EStatistic.SPIRIT: StatisticPoint(10, 100),
		 	EStatistic.STAMINA: StatisticPoint(10, 100)
		},
		{
			EAttack.PHYSICAL : PhysicalAttributes(5, 5),
		 	EAttack.SPIRITUAL: SpiritualAttributes(2, 2)
		}
	)
	entity_B: Entity = Entity(
		"B",
		{
			EStatistic.HEALTH : StatisticPoint(20, 100),
		 	EStatistic.SPIRIT : StatisticPoint(10, 100),
		 	EStatistic.STAMINA: StatisticPoint(10, 100)
		},
		{
			EAttack.PHYSICAL : PhysicalAttributes(5, 5),
		 	EAttack.SPIRITUAL: SpiritualAttributes(2, 2)
		}
	)
	battles: BattleSystem = BattleSystem(
		entity_A,
		entity_B
	)

	battles.start()
