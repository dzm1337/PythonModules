from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchanting(item_name: str) -> str:
        return enchantment_type + " " + item_name

    return enchanting


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    for i in range(1, 4):
        print(f"counter_a call {i}: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
