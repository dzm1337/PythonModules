from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.creatures import Sproutling, Bloomelle, Shiftling, Morphagon


def healing_creature_actions() -> None:

    factory = HealingCreatureFactory()
    sproutling = factory.create_base()
    bloomelle = factory.create_evolved()
    healing_creatures: list[Sproutling | Bloomelle] = [sproutling, bloomelle]
    i: int = 0

    print(" base :")
    for creatures in healing_creatures:
        if i == 1:
            print(" evolved :")
        print(creatures.describe())
        print(creatures.attack())
        print(creatures.heal())
        i += 1


def transform_creatures_actions() -> None:

    factory = TransformCreatureFactory()
    shiftling = factory.create_base()
    morphagon = factory.create_evolved()
    transform_creatures: list[Shiftling | Morphagon] = [shiftling, morphagon]
    i: int = 0

    print(" base :")
    for creature in transform_creatures:
        if i == 1:
            print(" evolved :")
        print(creature.describe())
        print(creature.attack())
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
        i += 1


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    healing_creature_actions()
    print(" ")
    print("Testing Creature with transform capability")
    transform_creatures_actions()
