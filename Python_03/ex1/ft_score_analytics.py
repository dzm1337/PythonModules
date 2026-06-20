from sys import argv


def score_parser(scores: list) -> bool:
    args_len: int = len(argv)
    if args_len == 1:
        print(
            f"No scores provided. Usage: python3 {argv[0]} "
            f"<score1> <score2> ..."
        )
        return False
    try:
        for arg in argv[1:]:
            scores.append(int(arg))
    except ValueError:
        for arg in argv[1:]:
            if type(arg) is not int:
                print(f"Invalid parameter: '{arg}'")
        print(
            f"No scores provided. Usage: python3 {argv[0]} "
            f"<score1> <score2> ..."
        )
        return False
    return True


def display_info_scores() -> None:
    scores: list[int] = []
    print("=== Player Score Analytics ===")
    if score_parser(scores):
        sum_score: int = sum(scores)
        len_score: int = len(scores)
        print(f"Scores processed: {scores}")
        print(f"Total Players: {len_score}")
        print(f"Total score: {sum_score}")
        print(f"Average score: {sum_score / len_score}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    display_info_scores()
