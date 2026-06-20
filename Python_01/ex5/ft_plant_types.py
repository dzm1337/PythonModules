class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} day(s) old")


class Flower(Plant):

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

    def bloom(self) -> None:
        if self.height >= 20:
            print(f"The {self.name} is blooming beautifully!")
        else:
            print(f"The {self.name} is not ready to bloom yet!")


class Tree(Plant):

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of {self.height:.1f}cm"
            f" long and {self.trunk_diameter:.1f}cm wide.\n"
        )


class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: int,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        print(
            f"{self.name}: {self.height:.1f}cm, {self.age} days old\n"
            f"Harvest season: {self.harvest_season}"
        )

    def display_extra_info(self) -> None:
        print(f"Nutritional value: {self.nutritional_value}")

    def grow_and_age(self, daily_growth: int, daily_aging: int) -> None:
        self.height += daily_growth
        self.age += daily_aging


if __name__ == "__main__":

    print("=== Garden Plant Types ===")

    plants: list[Plant] = [
        Flower("Rose", 15, 9, "red"),
        Flower("Rose", 25, 10, "red"),
        Tree("Oak", 200, 365, 5),
        Vegetable("Tomato", 5, 10, "April", 0),
        Vegetable("Tomato", 27, 10, "April", 20),
    ]

    print("=== Flower")
    plants[0].show()
    plants[0].bloom()
    print("[asking the rose to bloom]")
    plants[1].show()
    plants[1].bloom()

    print("\n=== Tree")
    plants[2].show()
    print("[asking the oak to produce shade]")
    plants[2].produce_shade()

    print("=== Vegetable")
    plants[3].show()
    plants[3].display_extra_info()
    print("[make tomato grow and age for 20 days]")

    plants[4].grow_and_age(20, 20)
    plants[4].show()
    plants[4].display_extra_info()
