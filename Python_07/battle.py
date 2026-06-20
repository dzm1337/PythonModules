import ex0


def verify_factory(factory: ex0.CreatureFactory) -> None:

    factory_base = factory.create_base()
    factory_evolved = factory.create_evolved()

    print(f"{factory_base.describe()}")
    print(f"{factory_base.attack()}")
    print(f"{factory_evolved.describe()}")
    print(f"{factory_evolved.attack()}")


def creature_fight(
    water: ex0.CreatureFactory, flame: ex0.CreatureFactory
) -> None:

    water_base = water.create_base()
    flame_base = flame.create_base()

    print(f"{flame_base.describe()}")
    print(" vs.")
    print(f"{water_base.describe()}")
    print(" fight!")
    print(f"{flame_base.attack()}")
    print(f"{water_base.attack()}")


if __name__ == "__main__":
    print("Testing Factory")
    verify_factory(ex0.FlameFactory())
    print("\nTesting Factory")
    verify_factory(ex0.WaterFactory())
    print("\nTesting battle")
    creature_fight(ex0.WaterFactory(), ex0.FlameFactory())
