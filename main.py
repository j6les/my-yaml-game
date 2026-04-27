from yaml_loader import load_yaml
from models import Player, Enemy
from game_engine import start_game

def main():
    # Load YAML data
    player_data = load_yaml("data/player.yaml")
    enemies_data = load_yaml("data/enemies.yaml")
    items_data = load_yaml("data/items.yaml")["items"]

    # Validate required fields (basic robustness)
    required_player_keys = ["name", "health", "attack", "inventory"]
    for key in required_player_keys:
        if key not in player_data:
            raise ValueError(f"Missing '{key}' in player.yaml")

    # Create objects
    player = Player(**player_data)
    enemies = [Enemy(**e) for e in enemies_data["enemies"]]

    # Start game
    start_game(player, enemies, items_data)


if __name__ == "__main__":
    main()