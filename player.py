# player.py
import json
from items import ITEMS

class Player:
    def __init__(self, name, health=100, attack=10, defense=5, level=1, xp=0, gold=0):
        self.name = name
        self.level = level
        self.xp = xp
        self.gold = gold

        self.max_hp = health
        self.hp = health
        self.attack = attack
        self.defense = defense

        # inventory is a dict: { item_name (str) : count (int) }
        self.inventory = {}

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "xp": self.xp,
            "gold": self.gold,
            "max_hp": self.max_hp,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "inventory": self.inventory.copy()
        }

    @classmethod
    def from_dict(cls, data):
        p = cls(
            name=data["name"],
            health=data["max_hp"],
            attack=data["attack"],
            defense=data["defense"],
            level=data["level"],
            xp=data["xp"],
            gold=data.get("gold", 0)
        )
        p.hp = data["hp"]
        p.inventory = data.get("inventory", {}).copy()
        return p

    def gain_xp(self, amount):
        self.xp += amount
        threshold = self.level * 100
        while self.xp >= threshold:
            self.xp -= threshold
            self.level_up()
            threshold = self.level * 100

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.attack += 3
        self.defense += 2
        self.hp = self.max_hp
        print(f"\n🎉 {self.name} reached level {self.level}! Stats increased:")
        print(f"    Max HP → {self.max_hp}, Attack → {self.attack}, Defense → {self.defense}\n")

    def take_damage(self, damage):
        actual = max(damage - self.defense, 1)
        self.hp = max(self.hp - actual, 0)
        return actual

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)

    def is_alive(self):
        return self.hp > 0

    def add_item(self, item_name, count=1):
        if item_name in self.inventory:
            self.inventory[item_name] += count
        else:
            self.inventory[item_name] = count

    def use_item(self, item_name):
        """Use a consumable item. Returns True if used, False otherwise."""
        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            print(f"❌ You don’t have any '{item_name}'.")
            return False

        info = ITEMS.get(item_name)
        if info is None or info.get("type") != "consumable":
            print(f"❌ '{item_name}' is not a consumable item.")
            return False

        # Apply effect
        heal_amount = info.get("heal", 0)
        if heal_amount > 0:
            self.heal(heal_amount)
            print(f"💊 You used {item_name} and restored {heal_amount} HP! (HP: {self.hp}/{self.max_hp})")

        # Decrement inventory
        self.inventory[item_name] -= 1
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
        return True

    def equip_item(self, item_name):
        """Equip weapon/armor. For simplicity, equipping permanently increases stats and removes from inventory."""
        if item_name not in self.inventory or self.inventory[item_name] <= 0:
            print(f"❌ You don’t have '{item_name}' to equip.")
            return False

        info = ITEMS.get(item_name)
        if info is None or info.get("type") not in ("weapon", "armor"):
            print(f"❌ '{item_name}' cannot be equipped.")
            return False

        att_bonus = info.get("attack_bonus", 0)
        def_bonus = info.get("defense_bonus", 0)

        self.attack += att_bonus
        self.defense += def_bonus
        print(f"🛡️  Equipped {item_name}! Attack +{att_bonus}, Defense +{def_bonus}.")
        # Remove from inventory
        self.inventory[item_name] -= 1
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]
        return True

    def show_inventory(self):
        if not self.inventory:
            print("📦 Your inventory is empty.")
            return
        print("📦 Inventory:")
        for item, cnt in self.inventory.items():
            print(f"   - {item} x{cnt}")
        print()

    def show_status(self):
        print(f"{self.name} (Lv.{self.level}) — HP: {self.hp}/{self.max_hp}  Attack: {self.attack}  Defense: {self.defense}  XP: {self.xp}/{self.level*100}  Gold: {self.gold}")

