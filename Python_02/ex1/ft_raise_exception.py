def input_temperature(data) -> int:
    temperature = int(data)
    if temperature > 40:
        raise Exception(f"{temperature}°C is"
                        f"too hot for plants (max 40°C)"
                        )
    if temperature < 0:
        raise Exception(f"{temperature}°C is"
                        f"too cold for plants (min 0°C)"
                        )
    return temperature


def test_temperature():
    test_values = ['25', 'abc', '100', '-50']
    for value in test_values:
        print(f"\nInput data is '{value}'")
        try:
            temperature = input_temperature(value)
            print(f"Temperature is now {temperature} °C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
