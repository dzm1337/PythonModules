from ex0.abstract_creatures import Creature


class Flameling(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Ember!"

    def describe(self) -> str:
        return super().describe()


class Pyrodon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses a Flamethrower!"

    def describe(self) -> str:
        return super().describe()


class Aquabub(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"

    def describe(self) -> str:
        return super().describe()


class Torragon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"

    def describe(self) -> str:
        return super().describe()
