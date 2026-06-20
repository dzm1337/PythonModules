from ex0.abstract_creatures import Creature, CreatureFactory
from ex2.abstract_strategy import BattleError, BattleStrategy


def battle(
    opponents_config: list[tuple[CreatureFactory, type[BattleStrategy]]],
) -> None:

    fighters: list[BattleStrategy] = []

    for factory, strategy_class in opponents_config:
        creature: Creature = factory.create_base()
        fighters.append(strategy_class(creature))

    print("*** Tournament ***")
    print(f"{len(fighters)} opponents involved\n")

    num_fighters = len(fighters)
    for i in range(num_fighters):
        for j in range(i + 1, num_fighters):
            f1 = fighters[i]
            f2 = fighters[j]
            print("* Battle *")
            print(f1.creature.describe())
            print("vs.")
            print(f2.creature.describe())
            print("now fight!")
        try:
            f1.act(f1.creature)
            f2.act(f2.creature)
        except BattleError as e:
            print(e)
            return


if __name__ == "__main__":
    from ex0.factory import FlameFactory, WaterFactory
    from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
    from ex2.strategies import (
        AggressiveStrategy,
        DefensiveStrategy,
        NormalStrategy,
    )

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    setup0 = [
        (FlameFactory(), NormalStrategy),
        (HealingCreatureFactory(), DefensiveStrategy),
    ]
    battle(setup0)
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    setup1 = [
        (FlameFactory(), AggressiveStrategy),
        (HealingCreatureFactory(), DefensiveStrategy),
    ]
    battle(setup1)
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    setup2 = [
        (WaterFactory(), NormalStrategy),
        (HealingCreatureFactory(), DefensiveStrategy),
        (TransformCreatureFactory(), AggressiveStrategy),
    ]
    battle(setup2)
