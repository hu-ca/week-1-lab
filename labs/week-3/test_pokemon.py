from pokemon import Pokemon, FireType, WaterType

def test_initial_current_hp_equals_max_hp():
    p = Pokemon("Eevee", 50,10,10, "Tackle", 40)
    assert p.current_hp == p.max_hp

def test_is_fainted_true_when_hp_zero():
    p = Pokemon("Eevee", 50, 10, 10, "Tackle", 40)
    p.current_hp = 0
    assert p.is_fainted() is True

def test_is_fainted_false_when_hp_above_zero():
    p = Pokemon("Eevee", 50, 10, 10, "Tackle", 40)
    p.current_hp = 1
    assert p.is_fainted() is False

def test_attack_move_returns_correct_format():
    p = Pokemon("Eevee", 50, 10, 10, "Tackle", 40)
    assert p.attack_move() == "Eevee uses Tackle!"

def test_firetype_description():
    f = FireType("Charmander", 39, 12, 8, "Ember", 40, 2)
    assert f.description() == "Charmander is a Fire type with 2% burn chance."

def test_watertype_description():
    w = WaterType("Squirtle", 44, 9, 10, "Water Gun", 40, 5)
    assert w.description() == "Squirtle is a Water type with swim speed 5."

def test_normaltype_description():
    p = Pokemon("Eevee", 50, 10, 10, "Tackle", 40)
    assert p.description() == "Eevee is a Normal type."


