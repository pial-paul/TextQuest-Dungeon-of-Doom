# 🕹️ TextQuest: A Console-Based Dungeon Crawler

**TextQuest** is a fun, intermediate-level Python project where players explore a procedurally generated dungeon, battle monsters, collect loot, and level up—all through a text-driven terminal interface. It’s a perfect next-step for learners who’ve mastered the basics and are ready to tackle object-oriented programming, data structures, and game loops.

---

## ✨ Key Features

- 🏰 **Procedural Dungeon Generation**  
  Explore a unique dungeon every time you start a new game, with monster rooms, treasure rooms, and a boss room.

- ⚔️ **Turn-Based Combat**  
  Battle skeletons, goblins, and orcs in strategic encounters where every decision counts.

- 🎒 **Inventory & Loot System**  
  Collect weapons, armor, potions, and gold. Equip items and manage your gear for survival.

- 🎮 **Player Progression**  
  Earn XP, level up, and improve your stats. Unlock new abilities and become dungeon royalty.

- 🧭 **Map Navigation**  
  Move through a grid-based dungeon using simple commands (`n`, `s`, `e`, `w`) and uncover what lurks within each room.

- 💾 **Save & Load**  
  Pick up where you left off with JSON-based save/load functionality.

- 👹 **Boss Fight & Victory Condition**  
  Defeat the final boss deep within the dungeon to win the game.

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.9 or later
- No external libraries needed (unless you want optional enhancements like color support)

### ▶️ Run the Game

```bash
python game.py
```

---

## 🎥 Demo Video

Want to see it in action? Watch the gameplay demo here:  
📺 [Watch on YouTube](https://youtu.be/B4NwbXLSjIw)


---

## 📁 Suggested File Structure

```
TextQuest/
├── game.py           # Main game loop & input handling
├── player.py         # Player class & progression logic
├── monster.py        # Monster classes (Goblin, Skeleton, etc.)
├── dungeon.py        # Dungeon generation & room logic
├── combat.py         # Turn-based combat mechanics
├── items.py          # Items & inventory system
├── save_load.py      # Save/load game data (JSON)
├── assets/           # Optional: ASCII art, flavor text, etc.
└── README.md         # You're reading it!
```

---

## 🧠 How It Works

### 🗺️ Dungeon Design

The dungeon is a 5×5 (or larger) grid of rooms, each randomly assigned as:

- **Empty**  
- **Monster Room**  
- **Treasure Room**  
- **Boss Room**

Procedural generation ensures there’s always a valid path from the entrance to the boss.

### 💥 Combat Mechanics

Each monster encounter is turn-based:

1. Choose to **Attack**, **Defend**, or **Use Item**  
2. Monster takes a turn (basic AI)  
3. Repeat until someone’s HP hits 0

Victory grants XP and possibly loot!

### 📦 Inventory System

Track items like:

```python
ITEMS = {
  "Health Potion": {"heal": 50, "type": "consumable"},
  "Iron Sword": {"attack_bonus": 5, "type": "weapon"},
  "Leather Armor": {"defense_bonus": 3, "type": "armor"},
}
```

You can use or equip items during or between fights.

---

## 🛠️ Optional Enhancements

- 🖍️ `colorama` support for colorful output (e.g., red for damage, green for healing)
- 🏪 Mini-shop system to buy/sell items
- 🧠 Smarter monster AI (defend, use potions, taunt)
- 🗺️ ASCII mini-map showing visited/unvisited rooms
- 🌫️ “Fog of war” system hiding unexplored areas

---

## 🔁 Sample Commands

- `n`, `s`, `e`, `w` — Move north, south, east, or west  
- `inventory` — Show your current items  
- `use [item]` — Use a potion or special item  
- `equip [item]` — Equip gear like swords or shields  
- `save` / `load` — Save or load game progress  

---

## 🎯 Educational Value

This project reinforces:

- ✅ Object-Oriented Design  
- ✅ Procedural Generation Algorithms  
- ✅ Game Loop Logic  
- ✅ File I/O & JSON Serialization  
- ✅ Combat & AI Systems  
- ✅ Strategic Thinking  

---

## 👨‍💻 Author

**Pial Paul**  
- 🔗 GitHub: [@pialpaul](https://github.com/pial-paul)  
- ✖️ X (Twitter): [@pialpaul](https://x.com/pial_paul_)  
- 💼 LinkedIn: [linkedin.com/in/pialpaul](https://linkedin.com/in/paulpial)  
- 📧 Email: [piaillaaa@gmail.com](mailto:piaillaaa@gmail.com)

---

## 📄 License

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### ⭐ Enjoying the game? Star this repo and share it with a fellow adventurer!
