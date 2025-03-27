import pick

def test_check_guess_correct():
    #setup
    answer = 5
    guess = 5
    expected = 0
    #invoke
    actual = pick.check_guess(guess, answer)
    #analyze
    assert expected == actual

def test_check_guess_too_low():
    #setup
    answer = 5
    guess = 7
    expected = 2
    #invoke
    actual = pick.check_guess(guess, answer)
    #analyze
    assert expected == actual

def test_check_guess_too_high():
    #setup
    answer = 9
    guess = 5
    expected = 4
    #invoke
    actual = pick.check_guess(guess, answer)
    #analyze
    assert expected == actual