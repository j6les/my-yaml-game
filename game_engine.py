import random

def use_item(player, enemy, items_data):
    if not player.inventory:
        print("No items available!")
        return

    print("\nInventory:")
    for i, item in enumerate(player.inventory):
        print(f"{i + 1}. {item}")

    try:
        choice = int(input("Choose item number: ")) - 1
        item_name = player.inventory[choice]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    item = items_data.get(item_name)

    if not item:
        print("Item not found in config.")
        return

    if item["type"] == "heal":
        player.health = min(player.max_health, player.health + item["value"])
        print(f"You used {item_name}! Healed for {item['value']}.")

    elif item["type"] == "damage":
        enemy.health -= item["value"]
        print(f"You used {item_name}! Dealt {item['value']} damage.")

    player.inventory.pop(choice)


def battle(player, enemy, items_data):
    print(f"\nA wild {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name}: {player.health} HP")
        print(f"{enemy.name}: {enemy.health} HP")

        action = input("Choose action (attack/item): ").lower()

        if action == "attack":
            enemy.health -= player.attack
            print(f"You attack {enemy.name} for {player.attack} damage!")

        elif action == "item":
            use_item(player, enemy, items_data)

        else:
            print("Invalid action.")
            continue

        if enemy.is_alive():
            player.health -= enemy.attack
            print(f"{enemy.name} attacks you for {enemy.attack} damage!")

    return player.is_alive()

def simulate_battle(player, enemy, items_data):
    # no input() version for CI/testing
    enemy.health = 0
    return True

def start_game(player, enemies, items_data):
    print("=== YAML RPG START ===")

    for enemy in enemies:
        if not player.is_alive():
            break

        won = battle(player, enemy, items_data)

        if won:
            print(f"You defeated {enemy.name}!")
        else:
            print("You were defeated...")
            return

    print("\nCongratulations! You beat all enemies!")