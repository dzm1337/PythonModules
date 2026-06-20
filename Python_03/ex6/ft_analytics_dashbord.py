import random


def ft_data_alchemist() -> None:
    raw_names: list[str] = [
        "Alice", "bob", "Charlie", "diana", "Emma",
        "frank", "Grace", "henry", "Iris", "jack",
        "Kate", "liam", "Maya", "noah", "Olivia",
        "peter", "Quinn", "rachel", "Samuel", "tara"
        ]

    names: list[str] = random.sample(raw_names, 7)
    print(f"Initial list of players = {names}")

    all_cap: list[str] = [name.capitalize() for name in names]
    print(f"New list with all names capitalized: {all_cap}")

    already_cap: list[str] = [name for name in names if name[0].isupper()]
    print(f"New_list of capitalized names only: {already_cap}")

    score_dict: dict[str, int] = {name: random.randrange(1, 1000)
                                  for name in all_cap}
    print(f"\nScore dict: {score_dict}")

    avg: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {avg:.2f}")

    high_score_dict: dict[str, int] = {name: score for name, score
                                       in score_dict.items() if score > avg}
    print(f"High scores: {high_score_dict}")


if __name__ == "__main__":
    ft_data_alchemist()
