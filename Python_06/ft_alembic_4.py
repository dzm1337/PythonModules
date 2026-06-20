import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Accessing the alchemy module using 'import alchemy'")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ")
    print(f"{alchemy.create_earth()}")
