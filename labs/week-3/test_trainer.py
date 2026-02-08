from pokemon import Pokemon, FireType, WaterType
from trainer import Trainer

def test_get_pokemon_by_type_fire():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))
    result = ash.get_pokemon_by_type(FireType)
    assert len(result) == 1
    assert isinstance(result[0], FireType)

def test_get_pokemon_by_type_water():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 0.2))
    ash.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))
    result = ash.get_pokemon_by_type(WaterType)
    assert len(result) == 1
    assert isinstance(result[1], WaterType)