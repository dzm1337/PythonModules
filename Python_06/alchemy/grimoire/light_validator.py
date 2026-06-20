def validate_ingredients(ingredients: str) -> str:
    from . import light_spellbook

    allowed: list[str] = light_spellbook.light_spell_allowed_ingredients()
    for allowed_ing in allowed:
        if allowed_ing in ingredients.lower():
            return "Earth, wind and fire - VALID"
    return "These ingredients shall not pass - INVALID"
