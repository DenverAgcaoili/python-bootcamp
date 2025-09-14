from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health=None, defense=None):
        self._health = health or 10
        self._defense = defense or 10

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()
