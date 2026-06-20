def ft_count_harvest_iterative():
    x = int(input("Days until harvest: "))
    for i in range(1, x + 1):
        if (i <= x):
            print(f"Day {i}")
    print("Harvest time!")
