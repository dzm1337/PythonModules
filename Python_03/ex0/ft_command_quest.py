from sys import argv


def info_argv():
    print("=== Command Quest ===")
    total_arg = len(argv)
    print(f"Program name: {argv[0]}")

    if total_arg == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_arg - 1}")
        i = 1
        for arg in argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total Arguments: {total_arg}")


if __name__ == "__main__":
    info_argv()
