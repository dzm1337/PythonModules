class PlantNameError(Exception):
    pass


def test_name_plant(name: str) -> None:
    if not 'A' <= name[0] <= 'Z':
        raise PlantNameError(f"Caught PlantError: Invalid "
                             f"plant name to water: '{name}'\n..."
                             f"ending tests and returning to main")
    print(f"Watering {name} [OK]")


def test_watering_system():
    print("=== Garden Watering System ===")

    plants = ["Tomato", "Lettuce", "Carrots"]
    print("\nTesting normal watering...")

    try:
        print("Opening watering system")
        for plant in plants:
            test_name_plant(plant)
    except PlantNameError as e:
        print(e)
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants...")
    plants_error = ["Tomato", "lettuce"]

    try:
        print("Opening watering system")
        for plant in plants_error:
            test_name_plant(plant)
    except PlantNameError as e:
        print(e)
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
