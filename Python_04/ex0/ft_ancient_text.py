from sys import argv
from typing import IO


def ft_ancient_text() -> None:
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <file>")
        return
    file_path: str = argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_path}'")

    file: IO | None = None
    try:
        file = open(file_path, "r")
        print("---")
        content: str = file.read()
        print(content, end="")
        print("---")
    except Exception as e:
        print(f"Error opening file: {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_path}' closed.")


if __name__ == "__main__":
    ft_ancient_text()
