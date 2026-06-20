from ex0.abstract_creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability

from ex2.abstract_strategy import BattleError, BattleStrategy


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(self.creature, Creature)

    def act(self, creature) -> None:
        if not self.is_valid(self.creature):
            raise BattleError(self.creature, self.__class__)
        creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(self.creature, TransformCapability)

    def act(self, creature) -> None:
        if not self.is_valid(self.creature):
            raise BattleError(self.creature, self.__class__)
        creature.attack()
        creature.transform()
        creature.attack()
        creature.revert()


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return isinstance(self.creature, HealCapability)

    def act(self, creature) -> None:
        if not self.is_valid(self.creature):
            raise BattleError(self.creature, self.__class__)
        creature.attack()
        creature.heal()
