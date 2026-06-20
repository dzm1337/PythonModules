class PlantStats:

    def __init__(self) -> None:
        self.grow_count = 0
        self.age_count = 0
        self.show_count = 0

    def display(self) -> None:
        print(
            f"Stats: {self.grow_count} grow, "
            f"{self.age_count} age, {self.show_count} show"
        )


class Plant:

    def __init__(
        self,
        name: str = "Unknown plant",
        height: float = 0.0,
        age: int = 0,
    ) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.stats = PlantStats()

    def grow(self, amount: float) -> None:
        self.height += amount
        self.stats.grow_count += 1

    def age_plant(self, days: int) -> None:
        self.age += days
        self.stats.age_count += 1

    def display_info(self) -> None:
        self.stats.show_count += 1
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def show_stats(self) -> None:
        self.stats.display()

    @staticmethod
    def check_year_old(days: int) -> bool:
        return days > 365


class Flower(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        if self.height >= 20:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def display_info(self) -> None:
        self.stats.show_count += 1
        print(
            f"{self.name}: {self.height:.1f}cm, {self.age} days old\n"
            f"Color: {self.color}"
        )


class Tree(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_count = 0

    def produce_shade(self) -> None:
        self.shade_count += 1
        print(
            f"Tree {self.name} now produces a shade of {self.height:.1f}cm"
            f" long and {self.trunk_diameter:.1f}cm wide."
        )

    def display_info(self) -> None:
        self.stats.show_count += 1
        print(
            f"{self.name}: {self.height:.1f}cm, {self.age} days old\n"
            f"Trunk diameter: {self.trunk_diameter:.1f}cm"
        )

    def show_stats(self) -> None:
        self.stats.display()
        print(f"{self.shade_count} shade")


class Seed(Flower):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        if self.age >= 60:
            print(f"{self.name} is blooming beautifully!")
            self.seeds = 42
        else:
            print(f"{self.name} has not bloomed yet")

    def display_info(self) -> None:
        self.stats.show_count += 1
        print(
            f"{self.name}: {self.height:.1f}cm, {self.age} days old\n"
            f"Color: {self.color}"
        )
        self.bloom()
        print(f"Seeds: {self.seeds}")


if __name__ == "__main__":

    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_year_old(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.display_info()
    rose.bloom()
    print("[statistics for Rose]")
    rose.show_stats()
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.display_info()
    rose.bloom()
    print("[statistics for Rose]")
    rose.show_stats()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.display_info()
    print("[statistics for Oak]")
    oak.show_stats()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.show_stats()

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.display_info()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age_plant(20)
    sunflower.display_info()
    print("[statistics for Sunflower]")
    sunflower.show_stats()

    print("\n=== Anonymous")
    anonymous = Plant()
    anonymous.display_info()
    print("[statistics for Unknown plant]")
    anonymous.show_stats()
