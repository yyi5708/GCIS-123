import pick

def test_check_guess_correct ():
    # setup
    answer = 5
    guess = 5
    expected = 0

    #invoke
    result = pick.check_guess (guess, answer)

    #analyze
    assert result == expected

def test_guess_too_high ():
    # setup
    answer = 5
    guess = 8
    expected = 2

    #invoke
    result = pick.check_guess (guess, answer)

    #analyze
    assert result == expected

def test_guess_too_low ():
    # setup
    answer = 5
    guess = 3
    expected = 2

    #invoke
    result = pick.check_guess (guess, answer)

    #analyze
    assert result == expected