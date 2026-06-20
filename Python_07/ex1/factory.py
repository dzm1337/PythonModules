from ex0.abstract_creatures import CreatureFactory
from ex1.creatures import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        sproutling = Sproutling("Sproutling", "Grass")
        return sproutling

    def create_evolved(self) -> Bloomelle:
        bloomelle = Bloomelle("Blomelle", "Grass/Fairy")
        return bloomelle


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        shiftling = Shiftling("Shiftling", "Normal")
        return shiftling

    def create_evolved(self) -> Morphagon:
        morphagon = Morphagon("Morphagon", "Normal/Dragon")
        return morphagon
