from .character import Character

class Warrior(Character):
    def __init__(self, strength, health=None, defense=None ):
        super().__init__(health,defense)
        self._strength = strength

    def attack(self, other):
        damage = self._strength - other._defense
        print(f"Damage is {damage}")
        other._health -= damage