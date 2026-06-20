def ft_count_harvest_recursive_helper(num):
    if num == 0:
        return
    ft_count_harvest_recursive_helper(num - 1)
    print(f"Day {num}")


def ft_count_harvest_recursive():
    num = int(input("Days until harvest: "))

    if num == 0:
        return
    else:
        ft_count_harvest_recursive_helper(num)
    print("Harvest Time!")
