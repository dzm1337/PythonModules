from abc import ABC, abstractmethod

from ex0.abstract_creatures import Creature


class BattleStrategy(ABC):
    def __init__(self, creature: Creature) -> None:
        self.creature = creature

    @abstractmethod
    def is_valid(self, creature: Creature):
        pass

    @abstractmethod
    def act(self, creature: Creature):
        pass


class BattleError(Exception):
    def __init__(
        self,
        creature: Creature,
        strategy_class: type,
    ) -> None:
        self.message = (
            f"Battle error, aborting tournament: "
            f"Invalid Creature '{creature.name}' "
            f"for this {strategy_class.__name__}"
        )
        super().__init__(self.message)
