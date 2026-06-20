import sys
from sys import argv
from typing import IO


def ft_stream_management() -> None:
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <file>")
        return

    file: IO | None = None
    file_path: str = argv[1]
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{argv[1]}'")
        file = open(file_path)
        original_content: str = file.read()
        print("---\n")
        print(original_content, end="")
        print("---")
    except Exception as e:
        print(f"[STDERR] Error opening file '{argv[1]}': {e}", file=sys.stderr)
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

    new_content: str = "".join(transformed_lines)

    print("Transform data:")
    print("---\n")
    print(new_content, end="")
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    raw_input: str = sys.stdin.readline()
    new_path: str = raw_input.strip()

    if not new_path:
        print("Not saving data.")
        return

    new_file: IO | None = None
    print(f"Saving data to '{new_path}'")
    try:
        new_file = open(new_path, "w")
        new_file.write(new_content)
        print(f"Data saved in file '{new_path}'")
    except Exception as e:
        print(
            f"[STDERR] Error opening file '{new_path}': {e}", file=sys.stderr
        )
        print("Data not saved")
        return
    finally:
        if new_file is not None:
            new_file.close()


if __name__ == "__main__":
    ft_stream_management()
