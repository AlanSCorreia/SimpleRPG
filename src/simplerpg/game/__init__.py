import simplerpg.engine as engine


def start() -> None:
    player: engine.logic.Entity = engine.logic.Entity(
        engine.logic.EntityTag.PLAYER,
        "Babador",
        engine.logic.StatisticPoints(
            engine.logic.Point(20, 20),
            engine.logic.Point(20, 20),
            engine.logic.Point(20, 20),
        ),
        engine.logic.AttributePoints(
            engine.logic.Point(5, 5),
            engine.logic.Point(5, 5),
            engine.logic.Point(5, 5),
            engine.logic.Point(5, 5)
        )
    )
    enemy: engine.logic.Entity = engine.logic.Entity(
        engine.logic.EntityTag.ENEMY,
        "Inimigo do Babador",
        engine.logic.StatisticPoints(
            engine.logic.Point(20, 20),
            engine.logic.Point(20, 20),
            engine.logic.Point(20, 20),
        ),
        engine.logic.AttributePoints(
            engine.logic.Point(5, 5),
            engine.logic.Point(5, 5),
            engine.logic.Point(5, 5),
            engine.logic.Point(5, 5)
        )
    )
    battle_system: engine.logic.BattleSystem = engine.logic.BattleSystem()
    battle_system.in_battle = True
    battle_system.on_battle_enter(
        player,
        enemy
    )

    while battle_system.in_battle:
        print(f"{player.name}: {player.statistic_points.health.current_value}", end=" "*20)
        print(f"{enemy.name}: {enemy.statistic_points.health.current_value}\n")
        
        print(f"Turn: {battle_system.turn:02}")
        print(f"Current Attacker: {battle_system.attacker.name}")

        battle_system.loop()

        if battle_system.turn == 15: break
    
    battle_system.on_battle_exit()
