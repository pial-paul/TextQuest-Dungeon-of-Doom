# save_load.py
import json
import os
from player import Player
from dungeon import Dungeon

SAVE_FILE = "savegame.json"

def save_game(player, dungeon):
    """
    Writes player and dungeon data to SAVE_FILE (JSON).
    """
    data = {
        "player": player.to_dict(),
        "dungeon": dungeon.to_dict()
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"\n✅ Game saved to '{SAVE_FILE}'.\n")

def load_game():
    """
    Loads and returns (player, dungeon). If SAVE_FILE does not exist, returns (None, None).
    """
    if not os.path.isfile(SAVE_FILE):
        print("❌ No save file found.")
        return None, None

    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    player = Player.from_dict(data["player"])
    dungeon = Dungeon.from_dict(data["dungeon"])
    print("✅ Loaded saved game.")
    return player, dungeon
