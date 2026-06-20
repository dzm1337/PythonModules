import alchemy

if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using 'import alchemy' strucure to access potions")
    print(
        f"Testing strenght_potion: "
        f"Strenght potion brewed with {alchemy.strength_potion()}"
    )
    print(f"Testing heal alias: Healing potion brewed with {alchemy.heal()}")
