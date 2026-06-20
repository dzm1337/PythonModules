from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type_creature: str) -> None:
        self.name = name
        self.type_creature = type_creature

    @abstractmethod
    def attack(self):
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type_creature} type Creature"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def create_evolved(self):
        pass
