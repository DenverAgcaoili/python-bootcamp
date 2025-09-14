from .character import Character

class Mage(Character):
    def __init__(self, magic, health=None, defense=None ):
        super().__init__(health,defense)
        self._magic = magic

    def attack(self, other):
        damage = (self._magic*2) - other._defense
        print(f"Damage is {damage}")
        other._health -= damage