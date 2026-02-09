from pokemon import Pokemon, FireType, WaterType
from trainer import Trainer

def test_get_pokemon_by_type_fire():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 2))
    ash.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))
    result = ash.get_pokemon_by_type(FireType)
    assert len(result) == 1
    assert isinstance(result[0], FireType)

def test_get_pokemon_by_type_water():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 2))
    ash.add_to_team(WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5))
    result = ash.get_pokemon_by_type(WaterType)
    assert len(result) == 1
    assert isinstance(result[1], WaterType)

def test_get_pokemon_by_type_empty():
    ash = Trainer("Ash")
    ash.add_to_team(FireType("Charmander", 39, 12, 8, "Ember", 40, 2))
    result = ash.get_pokemon_by_type(WaterType)
    assert result == []

def test_team_starts_empty():
    trainer = Trainer("Ash")
    assert trainer.get_team_size() == 0

def test_add_to_team_adds_pokemon_successfully():
    trainer = Trainer("Ash")
    p = FireType("Charmander", 10, 5, 2, "Ember", 40, 2)
    result = trainer.add_to_team(p)
    assert result is True
    assert trainer.get_team_size() == 1

def test_add_to_team_returns_false_when_team_full():
    trainer = Trainer("Ash")
    for i in range(6):
        assert trainer.add_to_team(
            FireType(f"Fire{i}", 10, 5, 2, "Ember", 40, 2)
        ) is True

    assert trainer.get_team_size() == 6
    assert trainer.add_to_team(WaterType("Squirtle", 10, 5, 2, "Water Gun", 40, 0)) is False


def test_add_to_team_returns_correct_count():
    trainer = Trainer("Ash")
    trainer.add_to_team(FireType("Charmander", 10,5, 2, "Ember", 40, 2))
    trainer.add_to_team(WaterType("Squirtle", 10, 5, 2, "Water Gun", 40, 0))
    trainer.add_to_team(FireType("Vulpix", 10, 5, 2, "Ember", 40, 2))

    assert trainer.get_team_size() == 3

def test_get_first_available_returns_first_non_fainted():
    trainer = Trainer("Ash")
    p1 = FireType("Charmander", 10, 5, 2, "Ember", 40, 2)
    p2 = WaterType("Squirtle", 10, 5, 2, "Water Gun", 40, 0)

    trainer.add_to_team(p1)
    trainer.add_to_team(p2)

    assert trainer.get_first_available() is p1


def test_get_first_available_skips_fainted_pokemon():
    trainer = Trainer("Ash")
    p1 = FireType("Charmander", 10, 5, 2, "Ember", 40, 2)
    p2 = WaterType("Squirtle", 10, 5, 2, "Water Gun", 40, 0)

    p1.current_hp = 0 

    trainer.add_to_team(p1)
    trainer.add_to_team(p2)

    assert trainer.get_first_available() is p2


def test_get_first_available_returns_none_when_all_fainted():
    trainer = Trainer("Ash")
    p1 = FireType("Charmander", 10, 5, 2, "Ember", 40, 2)
    p2 = WaterType("Squirtle", 10, 5, 2, "Water Gun", 40, 0)

    p1.current_hp = 0
    p2.current_hp = 0

    trainer.add_to_team(p1)
    trainer.add_to_team(p2)

    assert trainer.get_first_available() is None


def test_trainer_str_returns_correct_format():
    trainer = Trainer("Ash")
    trainer.add_to_team(FireType("Charmander", 10, 5, 2, "Ember", 40, 2))
    trainer.add_to_team(WaterType("Squirtle", 10, 5, 2, "Water Gun", 40, 0))

    assert str(trainer) == "Ash (2/6 Pokemon)"
