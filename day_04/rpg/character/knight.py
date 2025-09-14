from .character import Character

class Knight(Character):

    def attack(self, other):
        damage = (self._defense +5) - other._defense
        print(f"Damage is {damage}")
        other._health -= damage