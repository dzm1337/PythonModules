from ex0.abstract_creatures import Creature

from ex1.capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, type_creature: str) -> None:
        Creature.__init__(self, name, type_creature)

    def heal(self, target: str = "itself") -> str:
        return f"{self.name} heals {target} for a small amount"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def describe(self) -> str:
        return super().describe()


class Bloomelle(Creature, HealCapability):
    def __init_(self, name: str, type_creature: str) -> None:
        Creature.__init__(self, name, type_creature)

    def heal(self, target: str = "itself and others") -> str:
        return f"{self.name} heals {target} for a large amount"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def describe(self) -> str:
        return super().describe()


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type_creature: str) -> None:
        Creature.__init__(self, name, type_creature)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally"

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_trasnformed = False
        return f"{self.name} returns to normal."

    def describe(self) -> str:
        return super().describe()


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type_creature: str) -> None:
        Creature.__init__(self, name, type_creature)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its form."

    def describe(self) -> str:
        return super().describe()
