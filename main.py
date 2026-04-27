from yaml_loader import load_yaml
from models import Player, Enemy
from game_engine import start_game

def main():
    player_data = load_yaml("data/player.yaml")
    enemies_data = load_yaml("data/enemies.yaml")
    items_data = load_yaml("data/items.yaml")["items"]

    player = Player(**player_data)
    enemies = [Enemy(**e) for e in enemies_data["enemies"]]

    start_game(player, enemies, items_data)

if __name__ == "__main__":
    import sys

    if "ci" in sys.argv:
        print("CI MODE: running simulation only")
        
        # minimal smoke test (NO input())
        from yaml_loader import load_yaml
        from models import Player, Enemy

        player_data = load_yaml("data/player.yaml")
        enemies_data = load_yaml("data/enemies.yaml")

        player = Player(**player_data)
        enemies = [Enemy(**e) for e in enemies_data["enemies"]]

        print(f"Loaded player: {player.name}")
        print(f"Loaded {len(enemies)} enemies")
        print("CI SUCCESS")
    else:
        main()