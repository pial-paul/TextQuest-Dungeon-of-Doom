# game.py
import os
import sys
from player import Player
from dungeon import Dungeon
from combat import start_combat
from save_load import save_game, load_game

def clear_screen():
    """Cross-platform clear screen."""
    os.system("cls" if os.name == "nt" else "clear")

def prompt_movement():
    """Ask the player for a movement command."""
    print("\nMove: [N]orth  [S]outh  [E]ast  [W]est  [I]nventory  [S]ave  [Q]uit")
    return input("→ ").strip().lower()

def main():
    clear_screen()
    print("============================")
    print("   Welcome to TextQuest!   ")
    print("============================\n")

    # Main menu: New Game or Load Game
    while True:
        print("1) New Game")
        print("2) Load Game")
        print("3) Quit")
        choice = input("→ ").strip()
        if choice == "1":
            name = input("Enter your hero’s name: ").strip()
            player = Player(name=name)
            dungeon = Dungeon(size=5)
            dungeon.generate()
            print(f"\n🌟 Welcome, {player.name}. Your journey begins!\n")
            break
        elif choice == "2":
            player, dungeon = load_game()
            if player is None:
                continue  # no save found—back to menu
            else:
                print()
                break
        elif choice == "3":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.\n")

    # Starting position
    x, y = 0, 0
    dungeon.get_room(x, y).visited = True

    # Game loop
    while True:
        clear_screen()
        print("============================")
        print("       TextQuest RPG       ")
        print("============================\n")

        # Show player status and location
        player.show_status()
        print(f"Location: ({x}, {y})\n")

        current = dungeon.get_room(x, y)
        if current.room_type == "empty":
            if not current.visited:
                print("You enter an empty room. Nothing of interest here.")
                current.visited = True
        elif current.room_type == "monster":
            if not current.visited:
                print(f"You encountered a {current.monster.name}!")
                won = start_combat(player, current.monster)
                current.visited = True
                if won:
                    current.room_type = "empty"  # Monster defeated
                    current.monster = None
                else:
                    print("\nGame Over.")
                    break
        elif current.room_type == "treasure":
            if not current.visited:
                print("You found a treasure chest!")
                for item_name, count in current.loot.items():
                    player.add_item(item_name, count)
                    print(f"🎁 Collected {item_name} x{count}.")
                current.visited = True
                current.room_type = "empty"
                current.loot = {}
        elif current.room_type == "boss":
            if not current.visited:
                print(f"You have stumbled upon the final boss—{current.monster.name}!")
                won = start_combat(player, current.monster)
                current.visited = True
                if won:
                    print("\n🏅 Congratulations! You defeated the Dungeon Lord and cleared TextQuest!")
                    break
                else:
                    print("\nGame Over.")
                    break

        # If player is still alive and room has been processed, prompt next action
        if not player.is_alive():
            print("💀 You have fallen. Game Over.")
            break

        cmd = prompt_movement()
        if cmd in ("n", "north"):
            if x > 0:
                x -= 1
            else:
                print("🚧 You hit a wall. Can't move north.")
                input("\n(Press Enter to continue…)")

        elif cmd in ("s", "south"):
            if x < dungeon.size - 1:
                x += 1
            else:
                print("🚧 You hit a wall. Can't move south.")
                input("\n(Press Enter to continue…)")

        elif cmd in ("e", "east"):
            if y < dungeon.size - 1:
                y += 1
            else:
                print("🚧 You hit a wall. Can't move east.")
                input("\n(Press Enter to continue…)")

        elif cmd in ("w", "west"):
            if y > 0:
                y -= 1
            else:
                print("🚧 You hit a wall. Can't move west.")
                input("\n(Press Enter to continue…)")

        elif cmd in ("i", "inventory"):
            print()
            player.show_inventory()
            input("(Press Enter to continue…)")

        elif cmd in ("save", "s"):
            save_game(player, dungeon)
            input("(Press Enter to continue…)")

        elif cmd in ("quit", "q"):
            print("Are you sure you want to quit? Unsaved progress will be lost. (y/N)")
            confirm = input("→ ").strip().lower()
            if confirm == "y":
                print("Goodbye!")
                break

        else:
            print("❌ Invalid command.")
            input("\n(Press Enter to continue…)")

if __name__ == "__main__":
    main()
