# combat.py
from monster import Monster

def start_combat(player, monster):
    """
    Runs a turn-based combat loop between player and monster.
    Returns True if player wins, False if player dies.
    """
    print(f"\n⚔️  Combat started: {player.name} vs. {monster.name} (Lv.{monster.level})!")
    while player.is_alive() and monster.is_alive():
        # Show status
        print(f"\n{player.name} HP: {player.hp}/{player.max_hp}   {monster.name} HP: {monster.hp}/{monster.max_hp}")
        print("Choose action: [1] Attack   [2] Use Potion   [3] Flee")
        choice = input("→ ").strip()

        if choice == "1":
            damage = monster.take_damage(player.attack)
            print(f"➡️ You hit {monster.name} for {damage} damage!")
        elif choice == "2":
            # Try to use a health potion
            used = player.use_item("Health Potion") or player.use_item("Greater Health Potion")
            if not used:
                print("❌ No potion used. You wasted your turn.")
        elif choice == "3":
            # Attempt to flee: 50% chance
            import random
            if random.random() < 0.5:
                print("🏃 You successfully fled the battle!")
                return False  # treat as "no XP, no loot"
            else:
                print("❌ You failed to flee and lose your turn!")
        else:
            print("❌ Invalid choice, you lose your turn.")

        # Monster turn (if still alive)
        if monster.is_alive():
            m_dmg = monster.deal_damage()
            actual = player.take_damage(m_dmg)
            print(f"⚔️ {monster.name} hits you for {actual} damage! (HP: {player.hp}/{player.max_hp})")

    if player.is_alive() and not monster.is_alive():
        print(f"\n🏆 You defeated {monster.name}!")
        # Grant XP and gold reward
        player.gain_xp(monster.xp_reward)
        if monster.gold_reward > 0:
            player.gold += monster.gold_reward
            print(f"💰 You also looted {monster.gold_reward} gold!")
        return True
    else:
        print("\n💀 You have been defeated...")
        return False
