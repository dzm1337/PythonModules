from sys import argv
from typing import IO


def ft_archive_creation() -> None:
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <file>")
        return
    file_path: str = argv[1]
    file: IO | None = None
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{argv[1]}'")
        file = open(file_path, "r")
        original_content: str = file.read()
        print("---\n")
        print(original_content)
        print("\n---")
    except Exception as e:
        print(f"Error opening file '{argv[1]}': {e}")
        return
    finally:
        if file is not None:
            file.close()
            print(f"File '{argv[1]}' closed.\n")

    transformed_lines: list[str] = []
    current_line: str = ""

    for char in original_content:
        if char == "\n":
            current_line += "#" + "\n"
            transformed_lines.append(current_line)
            current_line = ""
        else:
            current_line += char

    if current_line != "":
        current_line += "#" + "\n"
        transformed_lines.append(current_line)

    new_content = "".join(transformed_lines)

    print("Transform data:")
    print("---\n")
    print(f"{new_content}", end="")
    print("\n---")

    new_path: str = str(input("Enter new file name (or empty): "))
    if not new_path:
        print("Not saving data.")
        return
    print(f"Saving data to '{new_path}'")
    new_file: IO | None = None
    try:
        new_file = open(new_path, "w")
        new_file.write(new_content)
        print(f"Data saved in file '{new_path}'")
    except Exception as e:
        print(f"Error saving file ''{new_path}': {e}")
    finally:
        if new_file is not None:
            new_file.close()


if __name__ == "__main__":
    ft_archive_creation()
