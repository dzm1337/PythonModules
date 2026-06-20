def ft_different_errors() -> None:
    try:
        print("Testing operation 0...")
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    try:
        print("Testing operation 1...")
        print(2 / 0)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    try:
        print("Testing operation 2...")
        open('/non/existent/file')
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    try:
        print("Testing operation 3...")
        print("4" + 4)
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    try:
        print("Testing operation 4...")
        4 + 4
    except (ValueError,
            FileNotFoundError,
            ZeroDivisionError,
            TypeError) as e:
        print(f"Caught: {e}")
    else:
        print("Operation completed successfully")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    ft_different_errors()
