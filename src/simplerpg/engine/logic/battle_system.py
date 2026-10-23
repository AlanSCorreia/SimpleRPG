import enum

from simplerpg.engine.logic import (
	entity,
	skills
)
import simplerpg.engine.visual as visual


class PlayerActionsInBattle(enum.Enum):
	ATTACK 	  = enum.auto()
	ABILITIES = enum.auto()
	INVENTORY = enum.auto()
	FLEE	  = enum.auto()


class BattleSystem:
	def __init__(
		self
	) -> None:

		self.turn: int = 0
		self.in_battle: bool = False
		self.attacker: entity.Entity | None = None
		self.defender: entity.Entity | None = None
	
	def __change_entities_roles(
		self
	) -> None:

		# Changes the roles of the entities in the actual turn of the battle
		temporary: entity.Entity = self.attacker
		self.attacker = self.defender
		self.defender = temporary

	def on_battle_enter(
		self,
		entity_player: entity.Entity,
		entity_npc: entity.Entity
	) -> None:

		self.attacker = entity_player
		self.defender = entity_npc

		self.in_battle = True
	
	def on_battle_exit(
		self
	) -> None:

		self.attacker = None
		self.defender = None

		self.turn = 0
	
	def check_if_battle_ended(
		self
	) -> None:

		print("Checando se o Defender morreu...")
		if self.defender.state is entity.EntityState.DEAD:
			self.in_battle = False
			print("Defender morreu, Fim da luta.")

	# TODO:
	# 	[ ] Give xp for the player
	#	[ ] If the player loses is game over
	def loop(
		self
	) -> None:

		# Ask what the player wants to do
		EntityBehaviorInBattle.calculate_entity_action(self)
		self.check_if_battle_ended()

		# Change entities roles and increase by one the turn count
		self.__change_entities_roles()
		self.turn += 1


class EntityBehaviorInBattle:
	@staticmethod
	def __has_entity_died(
		target_entity: entity.Entity
	) -> bool:

		return target_entity.state is PlayerState.DEAD

	@staticmethod
	def __ask_for_player_action(
		player_options_message: str="Escolha uma opção:"\
								   +"\n1) Lutar"\
								   +"\n1) Habilidades"\
								   +"\n2) Inventário"\
								   +"\n3) Fugir"\
								   +"\nopção escolhida -> "
	) -> PlayerActionsInBattle:

		# TODO: 
		#	[ ] put messages in a separate file in data
		#	[x] read the messages from parameters

		player_action: int = visual.Text.get_player_int_input(
			player_options_message,
			f"Opção inválida. {player_options_message}",
			(1, 2, 3)
		)
		actions = [action for action in PlayerActionsInBattle]

		return actions[player_action-1]
	
	@staticmethod
	def __entity_chooses_attack(
		battle_system: BattleSystem
	) -> None:

		damage: float = DamageSystem.calculate_damage(
			battle_system.attacker,
			battle_system.defender
		)

		battle_system.defender.statistic_points.health.current_value -= damage

		if battle_system.defender.statistic_points.health.current_value == 0:
			battle_system.defender.state = entity.EntityState.DEAD

	@staticmethod
	def __entity_chooses_abilities(
		battle_system: BattleSystem
	) -> None:

		#TODO: Implement
		print("To be implemented.")
	
	@staticmethod
	def __entity_chooses_inventory(
		battle_system: BattleSystem
	) -> None:

		#TODO: Implement
		print("To be implemented.")
	
	@staticmethod
	def __entity_chooses_flee(
		battle_system: BattleSystem
	) -> None:

		#TODO: Implement
		print("To be implemented.")
	
	@staticmethod
	def __calculate_entity_multiple_options(
		player_action: PlayerActionsInBattle,
		battle_system: BattleSystem
	) -> None:

		match player_action:
			case PlayerActionsInBattle.ATTACK	: __class__.__entity_chooses_attack(battle_system)
			case PlayerActionsInBattle.ABILITIES: __class__.__entity_chooses_abilities()
			case PlayerActionsInBattle.INVENTORY: __class__.__entity_chooses_inventory()
			case PlayerActionsInBattle.FLEE	  	: __class__.__entity_chooses_flee()
	
	@staticmethod
	def __calculate_player_action(
		battle_system: BattleSystem
	) -> None:

		# Get player decision
		player_action: PlayerActionsInBattle = __class__.__ask_for_player_action()

		# Compute his decision
		__class__.__calculate_entity_multiple_options(
			player_action,
			battle_system
		)
	
	@staticmethod
	def __calculate_enemy_action(
		battle_system: BattleSystem
	) -> None:

		#TODO: Implement more complex behavior
		__class__.__entity_chooses_attack(battle_system)
	
	@staticmethod
	def calculate_entity_action(
		battle_system: BattleSystem
	) -> None:

		print(battle_system.attacker.tag)
		match battle_system.attacker.tag:
			case entity.EntityTag.PLAYER: __class__.__calculate_player_action(battle_system)
			case entity.EntityTag.ENEMY: __class__.__calculate_enemy_action(battle_system)


class DamageSystem:
	@staticmethod
	def calculate_damage(
		attacker: entity.Entity,
		defender: entity.Entity
	) -> float:
		"""Calculate how much damage an entity causes to the other"""

		attacker_strength:   int = attacker.attribute_points.strength.current_value
		defender_resistence: int = defender.attribute_points.resistence.current_value

		# If an entity receives resistence buffs, this value should increase
		# Else, if receives debuffs, this value should decrease
		resistence_modifier: int = 100

		return attacker_strength*(100/(resistence_modifier+defender_resistence))
