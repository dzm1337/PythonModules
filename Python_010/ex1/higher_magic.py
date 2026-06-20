from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"A roaring fireball strikes {target} for {power} damage!"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP!"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spells(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined_spells


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        multiplied_power: int = power * multiplier
        print(f"Multiplying {power} power by {multiplier}x")
        return base_spell(target, multiplied_power)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def condition_verifier(target: str, power: int) -> str:
        if not condition(target, power):
            return "Spell fizzled"
        return spell(target, power)

    return condition_verifier


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell_results(target: str, power: int) -> list[str]:
        list_of_spells = []
        for spell in spells:
            list_of_spells.append(spell(target, power))
        return list_of_spells

    return spell_results


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"{' | '.join(combined('Dragon', 20))}")
    print()

    print("Testing power amplifier...")
    amplified_spell = power_amplifier(fireball, 10)
    print(f"{''.join(amplified_spell('Kraken', 25))}")
    print()

    print("Testing conditional caster...")
    condition: Callable[[str, int], bool] = lambda target, power: power > 50
    caster = conditional_caster(condition, fireball)
    print(caster("Charizard", 25))
    print(caster("Phoenix", 827))

    print("\nTesting spell sequence...")
    spells = [fireball, heal, fireball, heal]
    combo = spell_sequence(spells)
    results = combo("Charizard", 55)
    for r in results:
        print(r)
