# items.py

# A dictionary of all items in the game.
# Each item has a 'type' key that is one of: 'consumable', 'weapon', 'armor', 'misc'.
# Consumables have "heal" values; weapons/armors have attack_bonus/defense_bonus.

ITEMS = {
    "Health Potion": {
        "type": "consumable",
        "heal": 50
    },
    "Greater Health Potion": {
        "type": "consumable",
        "heal": 100
    },
    "Iron Sword": {
        "type": "weapon",
        "attack_bonus": 5
    },
    "Steel Sword": {
        "type": "weapon",
        "attack_bonus": 10
    },
    "Leather Armor": {
        "type": "armor",
        "defense_bonus": 3
    },
    "Chainmail Armor": {
        "type": "armor",
        "defense_bonus": 6
    },
    "Gold Coin": {
        "type": "misc"
    }
}
