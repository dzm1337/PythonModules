def secure_archive(
    filename: str,
    action: str = "read",
    content: str | None = None,
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                return (True, file.read())
        elif action == "write":
            if content is None:
                return (False, "Error: Missing content for write operation.")
            with open(filename, "w") as file:
                file.write(content)
                return (True, content)
        else:
            raise ValueError("Error: Not a valid action.")
    except Exception as e:
        return (False, f"{e}")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow", "read"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    with open("ancient_fragment.txt", "w") as f:
        f.write(
            "[FRAGMENT 001] Digital preservation protocols established 2087\n"
            "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
            "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
        )

    print(secure_archive("ancient_fragment.txt", "read"))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(
        secure_archive(
            "file.txt", "write", "Content successfully written to file"
        )
    )
