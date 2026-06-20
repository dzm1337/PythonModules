from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:

    if "INVALID" in validate_ingredients(ingredients):
        return (
            f"Spell Not Recorded {spell_name} "
            f"({validate_ingredients(ingredients)})"
        )
    return (
        f"Spell recorded: {spell_name} ({validate_ingredients(ingredients)})"
    )
