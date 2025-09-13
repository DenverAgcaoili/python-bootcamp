from abc import ABC, abstractmethod
from importlib.metadata import pass_none


class Character(ABC):
    def __init__(self, health=None, defense=None):
        self._health = health or 10
        self._defense = defense or 10

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

class Mage(Character):
    def __init__(self, magic, health=None, defense=None ):
        super().__init__(health,defense)
        self._magic = magic

    def attack(self, other):
        damage = (self._magic*2) - other._defense
        print(f"Damage is {damage}")
        other._health -= damage

class Knight(Character):

    def attack(self, other):
        damage = (self._defense +5) - other._defense
        print(f"Damage is {damage}")
        other._health -= damage


class Warrior(Character):
    def __init__(self, strength, health=None, defense=None ):
        super().__init__(health,defense)
        self._strength = strength

    def attack(self, other):
        damage = self._strength - other._defense
        print(f"Damage is {damage}")
        other._health -= damage

mage_1 = Mage(10,10,10)
knight_1 = Knight(10, 15)
warrior_1 = Warrior(10,10,10)


print(knight_1._health)
print(knight_1._defense)

mage_1.attack(knight_1)
print(knight_1._health)

 c


