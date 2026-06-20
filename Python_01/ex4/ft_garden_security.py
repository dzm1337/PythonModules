class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def show(self):
        print(
              f"Plant created: {self.name}: {self.__height}cm"
              f", {self.__age} days old"
        )

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self.__age = age
        print(f"Age updated: {self.__age} days\n")

    def set_height(self, height: int) -> None:
        if (height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self.__height = height
        print(f"\nHeight updated: {self.__height}cm")

    def get_age(self) -> int:
        return self.__age

    def get_height(self) -> int:
        return self.__height


if __name__ == "__main__":

    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 15, 10)

    plant1.show()
    plant1.set_height(25)
    plant1.set_age(30)
    plant1.set_height(-5)
    plant1.set_age(-4)
    height = plant1.get_height()
    age = plant1.get_age()

    print(f"\nCurrent plant: {plant1.name} {height:.1f}cm, {age} days")
