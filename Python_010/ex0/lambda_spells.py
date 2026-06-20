from typing import Any


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda k: k["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda k: k["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda k: "* " + k + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_val: int = max(mages, key=lambda k: k["power"])["power"]
    min_val: int = min(mages, key=lambda k: k["power"])["power"]
    avg: float = round(sum(map(lambda k: k["power"], mages)) / len(mages), 2)
    return {"max_power": max_val, "min_power": min_val, "avg_power": avg}


if __name__ == "__main__":
    artifacts: list[dict[str, Any]] = [
        {"name": "Mythic Book", "power": 827, "type": "legendary"},
        {"name": "Crystal Orb", "power": 150, "type": "epic"},
        {"name": "Shadow Dagger", "power": 85, "type": "rare"},
        {"name": "Lost Sword", "power": 46, "type": "rare"},
        {"name": "Flame Spell", "power": 31, "type": "common"},
        {"name": "Wooden Staff", "power": 12, "type": "common"},
        {"name": "Rusty Chain", "power": 5, "type": "common"},
    ]
    sorted_artifacts: list[dict[str, Any]] = artifact_sorter(artifacts)
    print("\nTesting artifact sorter...")
    for artifact in sorted_artifacts:
        print(
            f"{artifact['name']} - ({artifact['power']} power) - "
            f"{artifact['type']}"
        )

    print("\nTesting power filter...")
    min_power = 80
    filtered_artifacts = power_filter(artifacts, min_power)
    print(
        f"Artifacts must have at least {min_power} of power to be displayed..."
    )
    if filtered_artifacts:
        for artifact in filtered_artifacts:
            print(
                f"{artifact['name']} - ({artifact['power']} power) "
                f"- {artifact['type']}"
            )

    print("\nTesting spell transformer...")
    names: list[str] = []
    for item in artifacts:
        names.append(item["name"])
    print(" | ".join(spell_transformer(names)))

    print("\nTesting mage stats...")
    stats = mage_stats(artifacts)
    print(f"""Most powerful mage’s power level {stats["max_power"]}
Least powerful mage’s power level {stats["min_power"]}
Average power level (rounded to 2 decimals) {stats["avg_power"]}""")
