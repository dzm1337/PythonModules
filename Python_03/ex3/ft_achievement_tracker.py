import random


def ft_achievement_tracker():
    print("=== Achievement Tracker System ===")

    ALL_ACHIEVEMENTS = {
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer', 'Hidden Path Finder'
    }

    player_names = ["Alice", "Bob", "Charlie", "Dylan"]
    player_data = {}

    for name in player_names:
        num_to_grant = random.randint(5, 10)
        player_data[name] = set(
            random.sample(list(ALL_ACHIEVEMENTS), num_to_grant)
        )

    for name, achievements in player_data.items():
        print(f"\nPlayer {name}: {achievements}")

    all_distinct_achievements = set.union(*player_data.values())
    print(f"\nAll distinct achievements: {all_distinct_achievements}")

    common_achievements = set.intersection(*player_data.values())
    print(f"\nCommon achievements: {common_achievements}")

    for player_name, player_achievements in player_data.items():
        other_players_achievements = set()
        for other_name, other_achievements in player_data.items():
            if player_name != other_name:
                other_players_achievements.update(other_achievements)
        unique_to_player = player_achievements.difference(
            other_players_achievements
        )
        print(f"Only {player_name} has: {unique_to_player}")

    for player_name, player_achievements in player_data.items():
        missing = ALL_ACHIEVEMENTS.difference(player_achievements)
        print(f"{player_name} is missing: {missing}")


if __name__ == "__main__":
    ft_achievement_tracker()
