def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type_c = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{seed_type_c} seeds: {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{seed_type_c} seeds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{seed_type_c} seeds: covers {quantity} square meters")
    else:
        print(f"{seed_type_c} seeds: {quantity} unit(s)")
