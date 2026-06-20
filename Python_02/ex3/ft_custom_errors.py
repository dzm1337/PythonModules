class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant(name: str, watering_days: int) -> None:
    if watering_days < 4:
        raise PlantError(f"Caught PlantError: the {name} plant is wilting!")
    print(f"The {name} plant is healthy!")


def water_test(water: int) -> None:
    if water < 50:
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    print("There's enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    try:
        print("\nTesting PlantError...")
        test_plant("tomato", 3)
    except PlantError as e:
        print(e)

    try:
        print("\nTesting WaterError...")
        water_test(30)
    except WaterError as e:
        print(e)

    print(" ")
    print("Testing catching all garden errors...")
    errors: list[str] = ["test_water", "test_plant"]

    for error in errors:
        try:
            if error == "test_water":
                test_plant("tomato", 3)
            elif error == "test_plant":
                water_test(30)
        except GardenError as e:
            print(e)
    print("\nAll custom error types work correctly!")
