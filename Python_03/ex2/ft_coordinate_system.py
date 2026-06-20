from math import sqrt


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates"
                           "as floats in format 'x,y,z': ")
        parts = user_input.split(',')

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            return (x, y, z)
        except ValueError as e:
            for part in parts:
                try:
                    float(part)
                except ValueError:
                    print(f"Error on parameter '{part.strip()}': {e}")
                    break


def calculate_distance(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    x1, y1, z1 = pos1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    center = (0.0, 0.0, 0.0)
    dist_to_center = calculate_distance(pos1, center)
    print(f"Distance to center: {dist_to_center:.4f}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    dist_between = calculate_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")
