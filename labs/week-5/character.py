from operator import contains
from abc import ABC, abstractmethod
from exceptions import InvalidLivesError, InvalidCoinsError, CharacterDeadError

class Character(ABC):
    total_characters = 0

    def __init__(self, name: str, lives: int = 3, speed: float = 1.0) -> None:
        self._name = name
        self._lives = lives
        self._coins = 0
        self._speed = speed
        Character.total_characters += 1
        pass

    @property
    def name(self):
        return self._name

    def lives(self, value: int):
        if 0 <= value <= 99:
            raise InvalidLivesError("Lives must be between 0 and 99")

    def coins(self, value: int):
        if 0 <= value <= 999:
            raise InvalidCoinsError("Coins must be between 0 and 999")

    def is_alive(self):
        return self._lives > 0

    def collect_coin(self):
        if 0 <= self._coins < 100:
            self._coins += 1
        else:
            self._coins = 0
            self._lives += 1    

    def take_damage(self):
        if self._lives == 0:
            raise CharacterDeadError(f"{self._name} has no lives remaining!")
        else:
            self._lives -= 1
    
    



