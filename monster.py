# monster.py
import random

class Monster:
    def __init__(self, name, level, health, attack, defense, xp_reward, gold_reward=0):
        self.name = name
        self.level = level
        self.max_hp = health
        self.hp = health
        self.attack = attack
        self.defense = defense
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        actual = max(damage - self.defense, 1)
        self.hp = max(self.hp - actual, 0)
        return actual

    def deal_damage(self):
        # Monster always deals at least 1
        return self.attack

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "attack": self.attack,
            "defense": self.defense,
            "xp_reward": self.xp_reward,
            "gold_reward": self.gold_reward
        }

    @classmethod
    def from_dict(cls, data):
        m = cls(
            name=data["name"],
            level=data["level"],
            health=data["max_hp"],
            attack=data["attack"],
            defense=data["defense"],
            xp_reward=data["xp_reward"],
            gold_reward=data.get("gold_reward", 0)
        )
        m.hp = data["hp"]
        return m


# Factory functions to generate different monsters

def random_monster(depth_level=1):
    """
    Generate a random monster based on dungeon depth (1 = easy, higher = harder).
    Returns an instance of Monster.
    """
    choices = ["Goblin", "Skeleton", "Orc"]
    name = random.choice(choices)

    # Scale stats by depth_level
    base = depth_level * 10
    if name == "Goblin":
        hp = base + random.randint(5, 10)
        attack = depth_level * 2 + random.randint(1, 3)
        defense = depth_level * 1 + random.randint(0, 1)
        xp_reward = depth_level * 20
        gold_reward = random.randint(5, 10) * depth_level
    elif name == "Skeleton":
        hp = base + random.randint(8, 15)
        attack = depth_level * 3 + random.randint(1, 2)
        defense = depth_level * 2 + random.randint(0, 1)
        xp_reward = depth_level * 30
        gold_reward = random.randint(10, 15) * depth_level
    else:  # Orc
        hp = base + random.randint(12, 20)
        attack = depth_level * 4 + random.randint(2, 4)
        defense = depth_level * 2 + random.randint(1, 2)
        xp_reward = depth_level * 40
        gold_reward = random.randint(15, 20) * depth_level

    return Monster(name=name, level=depth_level, health=hp, attack=attack, defense=defense, xp_reward=xp_reward, gold_reward=gold_reward)


def boss_monster():
    """
    Generate the final boss. Stats are higher.
    """
    name = "Dungeon Lord"
    hp = 200
    attack = 20
    defense = 10
    xp_reward = 500
    gold_reward = 100
    return Monster(name=name, level=5, health=hp, attack=attack, defense=defense, xp_reward=xp_reward, gold_reward=gold_reward)
