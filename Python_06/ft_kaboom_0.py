import alchemy.grimoire

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    test: str = alchemy.grimoire.light_spell_record("Fantasy", "monkey")
    test2: str = alchemy.grimoire.light_spell_record(
        "Fantasy", "EARTH, WIND and FIRE"
    )
    print(f"Testing record light spell: {test}")
    print(f"Testing record light spell: {test2}")
