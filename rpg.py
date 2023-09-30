import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.inventory = []

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        actual_damage = max(damage - enemy.defense, 0)
        enemy.take_damage(actual_damage)
        return actual_damage

    def heal(self):
        healing = random.randint(10, 20)
        self.health = min(100, self.health + healing)
        return healing

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = 2

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def attack_player(self, player):
        damage = random.randint(0, self.attack)
        actual_damage = max(damage - player.defense, 0)
        player.take_damage(actual_damage)
        return actual_damage

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Dungeon:
    def __init__(self):
        self.player = None
        self.enemies = []
        self.items = []

    def add_player(self, player):
        self.player = player

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def add_item(self, item):
        self.items.append(item)

def main():
    print("Welcome to the Dungeon Adventure!")

    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    dungeon = Dungeon()
    dungeon.add_player(player)

    enemy1 = Enemy("Goblin", 20, 8)
    enemy2 = Enemy("Orc", 30, 12)
    dungeon.add_enemy(enemy1)
    dungeon.add_enemy(enemy2)

    potion = Item("Health Potion", "Restores 20 health points.")
    sword = Item("Sword", "Increases attack damage by 5.")
    dungeon.add_item(potion)
    dungeon.add_item(sword)

    while player.is_alive():
        print("\nOptions:")
        print("1. Explore")
        print("2. Check Inventory")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            if random.random() < 0.5:
                enemy = random.choice(dungeon
