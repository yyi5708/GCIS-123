import dog_age

def test_humans_years_negative_one():
    
    #setup
    years = -1
    expected = (None)
    #invoke
    actual = dog_age.human_years(years)
    #analyze
    assert expected == actual

def test_humans_years_zero():

    #setup
    years = 0
    expected = (None)
    #invoke
    actual = dog_age.human_years(years)
    #analyze
    assert expected == actual

def test_humans_years_one():

    #setup
    years = 1
    expected = (15)
    #invoke
    actual = dog_age.human_years(years)
    #analyze
    assert expected == actual

def test_humans_years_two():

    #setup
    years = 2
    expected = (24)
    #invoke
    actual = dog_age.human_years(years)
    #analyze
    assert expected == actual

def test_humans_years_three():

    #setup
    years = 3
    expected = (29)
    #invoke
    actual = dog_age.human_years(years)
    #analyze
    assert expected == actual

#DONE.