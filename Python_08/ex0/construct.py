import os
import site
import sys

if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("""SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.""")
        print("\nPackage installation path: ")
        print(f"{site.getsitepackages()[0]}")
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Envirnment: None detected\n")
        print("WARNING: You're in the global envionment!")
        print("The machines can see everything you install.\n")
        print("""To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env/Scripts/activate # On Windows\n
Then run this program again.""")
