from character.knight import Knight
from character.mage import Mage
from character.warrior import Warrior

mage_1 = Mage(10,10,10)
knight_1 = Knight(10, 15)
warrior_1 = Warrior(10,10,10)


print(knight_1._health)
print(knight_1._defense)

mage_1.attack(knight_1)
print(knight_1._health)