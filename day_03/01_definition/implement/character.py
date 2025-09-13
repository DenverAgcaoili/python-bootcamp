class Character:
    def __init__(self,health=10, strength=10, defense=10):
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self,other):
        damage = self.strength - other.defense
        print(f"Damage is {damage}")
        other.health -= damage

player = Character(strength=11)
enemy = Character()

print(enemy.health)

player.attack(enemy)
print(enemy.health)


player.attack(enemy)
print(enemy.health)