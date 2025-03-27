import alliteration

def test_empty_string():
    # setup
    sentence = ""

    # invoke
    try:
        alliteration.is_alliteration(sentence)
        assert False, "Expected exception"

    # analzye
    except ValueError:
        assert True

def test_single_word():
    # setup
    sentence = "Dog"

    # invoke
    try:
        alliteration.is_alliteration(sentence)
        assert False, "Expected exception"

    # analzye
    except ValueError:
        assert True

def test_two_words_true():
    # setup
    sentence = "Dog days"
    expected = True

    # invoke
    actual = alliteration.is_alliteration(sentence)

    # analzye
    assert expected == actual

def test_two_words_false():
    # setup
    sentence = "Cat nights"
    expected = False

    # invoke
    actual = alliteration.is_alliteration(sentence)

    # analzye
    assert expected == actual

def test_sentence_true():
    # setup
    sentence = "Betty Babbage bought butter before baking banana bread."
    expected = True

    # invoke
    actual = alliteration.is_alliteration(sentence)

    # analzye
    assert expected == actual

def test_sentence_false():
    # setup
    sentence = "Tommy the turtle ran terribly."
    expected = False

    # invoke
    actual = alliteration.is_alliteration(sentence)

    # analzye
    assert expected == actual

#Done