class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"Created: {self.name} {self.height:.1f}cm, {self.age} days old")


if __name__ == "__main__":
    plants = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Oak", "height": 200, "age": 365},
        {"name": "Cactus", "height": 5, "age": 90},
        {"name": "Sunflower", "height": 80, "age": 45},
        {"name": "Fern", "height": 15, "age": 120}
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        Plant(plant["name"], plant["height"], plant["age"]).get_info()
