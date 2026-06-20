import random
import time
from collections.abc import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self, power: int, *args, **kwargs):
            if power >= min_power:
                return func(self, power, *args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


@spell_timer
def fireball() -> str:
    time.sleep(0.2)
    return "Result: Fireball cast!"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@retry_spell(max_attempts=3)
def summon_familiar():
    if random.random() < 0.7:
        raise Exception("Familiar didn't hear the call")
    return "An Owl has arrived!"


if __name__ == "__main__":
    print("=== Test: Spell Timer ===")
    print(fireball())

    print("\n=== Test: MageGuild ===")
    mage = MageGuild()
    names = ["An", "Diogo", "John-Smith", "John Smith"]
    for n in names:
        status = "Valid" if mage.validate_mage_name(n) else "Invalid"
        print(f"Mago '{n}': {status}")

    print("\n=== Testing Cast Spell (Power Validator) ===")
    print(mage.cast_spell(50, "Meteor"))
    print(mage.cast_spell(5, "Spark"))

    print("\n=== Testing Retry Spell ===")
    print(summon_familiar())
