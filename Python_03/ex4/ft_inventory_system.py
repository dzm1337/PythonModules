import sys


def ft_inventory_system() -> None:
    argv = sys.argv[1:]

    print("=== Inventory System Analysis ===")
    inventory = {}
    try:
        if len(argv) < 1:
            raise Exception("Error: Not enough arguments")
    except Exception as e:
        print(e)
        return
    for arg in argv:
        try:
            if ":" not in arg:
                raise Exception(f"Error - invalid parameter '{arg}'")
            data = arg.split(":")
            if len(data) != 2:
                raise Exception(f"Error - invalid parameter '{arg}'")
            name = data[0]
            quantity_str = data[1]
            if name in inventory:
                raise Exception(f"Redundant item '{name}' - discarding")
            try:
                quantity = int(quantity_str)
                inventory.update({name: quantity})
            except ValueError:
                print(f"Quantity error for '{name}': invalid "
                      f"literal for int() with base 10: '{quantity_str}'")
        except Exception as e:
            print(e)

    print(f"Got inventory: {inventory}")

    keys_list = list(inventory.keys())
    print(f"Item list: {keys_list}")

    total_values = sum(list(inventory.values()))
    item_count = len(keys_list)
    print(f"Total quantity of the {item_count} items: {total_values}")

    for item, value in inventory.items():
        percentage = round((value / total_values) * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most = keys_list[0]
    least = keys_list[0]
    for item, value in inventory.items():
        if value > inventory[most]:
            most = item
        if value < inventory[least]:
            least = item

    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
