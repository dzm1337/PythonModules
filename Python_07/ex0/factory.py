from ex0.abstract_creatures import Creature, CreatureFactory
from ex0.creatures import Aquabub, Flameling, Pyrodon, Torragon


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        flameling = Flameling("Flameling", "Fire")
        return flameling

    def create_evolved(self) -> Creature:
        pyrodon = Pyrodon("Pyrodon", "Fire/Flying")
        return pyrodon


class WaterFactory(CreatureFactory):
    def create_base(self) -> Creature:
        aquabub = Aquabub("Aquabub", "Water")
        return aquabub

    def create_evolved(self) -> Creature:
        torragon = Torragon("Torragon", "Water")
        return torragon
