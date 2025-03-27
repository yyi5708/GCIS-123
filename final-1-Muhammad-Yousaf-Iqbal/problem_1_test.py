from problem_1 import *

def test_planet_init():
    try:
        Planet('Name1', 100, 200)
        assert True
    except:
        assert False

def test_planet_get_name():
    planet_1 = Planet('Name1', 100, 200)
    assert planet_1.get_name() == 'Name1'

def test_planet_get_size():
    planet_1 = Planet('Name1', 100, 200)
    assert planet_1.get_size() == 100

def test_planet_get_orbit():
    planet_1 = Planet('Name1', 100, 200)
    assert planet_1.get_orbit() == 200

def test_planet_repr():
    planet_1 = Planet('Name1', 100, 200)
    assert repr(planet_1) == 'Name1:100:200'

def test_planet_eq():
    planet_1 = Planet('Name1', 100, 200)
    planet_2 = Planet('Name2', 100, 200)
    planet_3 = Planet('Name3', 200, 400)
    assert planet_1 == planet_2
    assert not(planet_1 == planet_3)
    assert not(planet_1 == None)

def test_planet_lt():
    try:
        planet_1 = Planet('Name1', 100, 200)
        planet_2 = Planet('Name2', 100, 200)
        planet_3 = Planet('Name3', 200, 400)
        assert planet_2 < planet_3
        assert not(planet_3 < planet_2)
        assert not(planet_1 < None)
        planet_list = [planet_1, planet_2, planet_3]
        planet_list.sort()
        assert True
    except:
        assert False

def test_planet_hash():
    try:
        planet_1 = Planet('Name1', 100, 200)
        planet_2 = Planet('Name2', 100, 200)
        planet_3 = Planet('Name3', 200, 400)
        planet_list = [planet_1, planet_2, planet_3]
        set(planet_list)
        assert True
    except:
        assert False

def test_planets_init():
    try:
        Planets('data/planets.csv')
        assert True
    except:
        assert False

def test_planets_get_names():
    try:
        planetDB = Planets('data/planets.csv')
        assert planetDB.get_names() == ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
    except:
        assert False

def test_planets_get_planet():
    try:
        planetDB = Planets('data/planets.csv')
        assert planetDB.get_planet('Earth').get_name() == 'Earth'
        assert planetDB.get_planet('Earth').get_size() == 3959
        assert planetDB.get_planet('Earth').get_orbit() == 93000000
        assert planetDB.get_planet('Unknown') == None
    except:
        assert False

def test_planets_get_orbit_delta():
    try:
        planetDB = Planets('data/planets.csv')
        assert planetDB.get_orbit_delta('Jupiter','Earth') == 390600000
        assert planetDB.get_orbit_delta('Jupiter','Unknown') == None
    except:
        assert False

