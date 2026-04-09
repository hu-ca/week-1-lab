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
    
    @abstractmethod
    def jump():
        """Subclasses implement their jump style"""
        pass
    
    def run():
        """Subclasses implement their run style"""
        pass

    def special_ability():
        """Subclasses implement their unique ability"""
        pass

    def get_total_characters():
        return Character.total_characters

class Mario(Character):

    def __init__(self):
        super().__init__("Mario", 3, 1.0)

    def jump(self):
        return "Mario jumps!"

    def run(self):
        return "Mario runs at normal speed!"

    def special_ability(self):
        return "Mario uses fireball!"

class Luigi(Character):
    
    def __init__(self, lives):
        super().__init__("Luigi", 3, 0.9)

    def jump(self):
        return "Luigi jumps higher and floatier!"

    def run(self):
        return "Luigi runs with slippery momentum!"
    
    def special_ability(self):
        return "Luigi uses Poltergust!"

class Peach(Character):

    def __init__(self):
        super().__init__("Peach", 3, 0.85)

    def jump(self):
        return "Peach floats gracefully through the air!"

    def run(self):
        return "Peach runs elegantly!"

    def special_ability(self):
        return "Peach uses her parasol!"

class Toad(Character):
    
    def __init__(self):
        super().__init__("Toad", 3, 1.2)

    def jump(self):
        return "Toad does a short but quick jump!"

    def run(self):
        return "Toad zooms ahead!"

    def special_ability(self):
        return "Toad uses spore burst!"

