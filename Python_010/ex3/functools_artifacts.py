from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    valid_operations: dict[str, Callable[[int, int], int]] = {
        "multiply": mul,
        "add": add,
        "max": max,
        "min": min,
    }
    if operation not in valid_operations:
        raise ValueError("ERROR: Invalid Operator")
    return reduce(valid_operations[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchanting {target} with {element} power of {power}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchantments: dict[str, Callable] = {
        "fire": partial(base_enchantment, 50, "Fire"),
        "ice": partial(base_enchantment, 50, "Ice"),
        "thunder": partial(base_enchantment, 50, "Thunder"),
    }
    return enchantments


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base_dispatch(x: Any) -> str:
        return "Unknown spell"

    @base_dispatch.register(int)
    def _(x: int) -> str:
        return f"Damage spell: {x} damage"

    @base_dispatch.register(str)
    def _(x: str) -> str:
        return f"Enchantment: {x}"

    @base_dispatch.register(list)
    def _(x: list[Any]) -> str:
        return f"Multicast: {len(x)} spell(s)"

    return base_dispatch


@lru_cache(maxsize=3)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    operations: list[str] = ["max", "add", "multiply", "min", "unknown"]
    numbers: list[int] = [21, 65, 53, 34, 12, 42]
    empty: list[int] = []

    print("\nTesting spell_reducer...")
    try:
        for op in operations:
            print(f"{op}: {spell_reducer(numbers, op)}")
    except ValueError as e:
        print(e)
    print(f"Empty list: {spell_reducer(empty, 'max')}")

    print("\nTesting partial_enchanter...")
    enchant = partial_enchanter(base_enchantment)
    print(enchant["fire"]("Sword"))
    print(enchant["ice"]("Helmet"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch({}))
