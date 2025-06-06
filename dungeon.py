# dungeon.py
import random
import json
from monster import random_monster, boss_monster
from items import ITEMS

class Room:
    """
    Represents a single room in the dungeon.
    Attributes:
        x, y: coordinates in the grid.
        room_type: 'empty' | 'monster' | 'treasure' | 'boss'
        visited: bool
        monster: Monster object if room_type == 'monster' or 'boss'
        loot: dict { item_name: count } if room_type == 'treasure'
    """
    def __init__(self, x, y, room_type="empty"):
        self.x = x
        self.y = y
        self.room_type = room_type
        self.visited = False
        self.monster = None
        self.loot = {}

        if room_type == "monster":
            # depth_level = max(x, y) // 1 + 1  (for simplicity, use x+y+1)
            depth = (x + y) // 2 + 1
            self.monster = random_monster(depth_level=depth)
        elif room_type == "boss":
            self.monster = boss_monster()
        elif room_type == "treasure":
            # Randomly pick 1–2 items from ITEMS that are consumable or misc
            choices = [k for k,v in ITEMS.items() if v["type"] in ("consumable", "misc")]
            for _ in range(random.randint(1, 2)):
                item = random.choice(choices)
                if item in self.loot:
                    self.loot[item] += 1
                else:
                    self.loot[item] = 1

    def to_dict(self):
        data = {
            "x": self.x,
            "y": self.y,
            "room_type": self.room_type,
            "visited": self.visited,
            "loot": self.loot.copy()
        }
        if self.monster:
            data["monster"] = self.monster.to_dict()
        else:
            data["monster"] = None
        return data

    @classmethod
    def from_dict(cls, data):
        room = cls(data["x"], data["y"], room_type=data["room_type"])
        room.visited = data["visited"]
        room.loot = data.get("loot", {}).copy()
        if data.get("monster"):
            # Reconstruct monster
            from monster import Monster
            room.monster = Monster.from_dict(data["monster"])
        else:
            room.monster = None
        return room


class Dungeon:
    """
    Generates a square dungeon of size N x N.
    Room types are randomly assigned but ensure:
      - Start at (0,0) is 'empty'
      - Boss at (N-1, N-1)
      - Other rooms: randomly 'empty', 'monster', or 'treasure'
    """
    def __init__(self, size=5):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def generate(self):
        for i in range(self.size):
            for j in range(self.size):
                if i == 0 and j == 0:
                    room_type = "empty"
                elif i == self.size - 1 and j == self.size - 1:
                    room_type = "boss"
                else:
                    roll = random.random()
                    if roll < 0.4:
                        room_type = "empty"
                    elif roll < 0.75:
                        room_type = "monster"
                    else:
                        room_type = "treasure"
                self.grid[i][j] = Room(x=i, y=j, room_type=room_type)

    def get_room(self, x, y):
        return self.grid[x][y]

    def to_dict(self):
        return {
            "size": self.size,
            "rooms": [
                [self.grid[i][j].to_dict() for j in range(self.size)]
                for i in range(self.size)
            ]
        }

    @classmethod
    def from_dict(cls, data):
        size = data["size"]
        d = cls(size=size)
        for i in range(size):
            for j in range(size):
                room_data = data["rooms"][i][j]
                d.grid[i][j] = Room.from_dict(room_data)
        return d
