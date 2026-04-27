class Player:
    def __init__(self, name, health, attack, inventory):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.inventory = inventory

    def is_alive(self):
        return self.health > 0


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0