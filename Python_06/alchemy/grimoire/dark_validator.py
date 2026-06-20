from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    for allowed_ing in allowed:
        if allowed_ing in ingredients.lower():
            return "Bats, Frogs and Arsenic - VALID"
    return "These ingredients shall not pass - INVALID"
