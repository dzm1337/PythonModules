def check_temperature(temp_str: str) -> None:
    try:
        temp_int = int(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    else:
        print(f"Temperature is now {temp_int}°C")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    temperatures: list = [25, 'abc']
    for temp in temperatures:
        print(f"Input data is '{temp}'")
        check_temperature(temp)
        print(" ")
    print("All tests completed - program didn't crash!")
