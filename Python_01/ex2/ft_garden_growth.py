class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age:.0f} days old")

    def grow(self, daily_aging: int, daily_growth: int) -> None:
        self.age += daily_aging
        self.height += daily_aging * daily_growth


if __name__ == "__main__":

    plant = Plant("Rose", 25, 30)
    i = 1
    daily_aging = 0.8
    growth = 0
    for _ in range(1, 8):
        print(f"=== Day {i} ===")
        plant.get_info()
        plant.grow(daily_aging, 1)
        i += 1
        growth += daily_aging
    print(f"Growth this week: {growth - daily_aging:.1f}cm")
