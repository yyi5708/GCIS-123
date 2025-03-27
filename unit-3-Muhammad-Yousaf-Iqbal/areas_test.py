import areas

def test_square_8():
    #setup
    length = 8
    expected = 64
    #invoke
    actual = areas.square(length)
    #analyze
    assert actual == expected

def test_square_16():
    #setup
    length = 16
    expected = 256
    #invoke
    actual = areas.square(length)
    #analyze
    assert actual == expected

def test_rectangle_5_7():
    #setup
    width = 5
    height = 7
    expected = 35
    #invoke
    actual = areas.rectangle(width, height)
    #analyze
    assert actual == expected

def test_rectangle_10_14():
    #setup
    width = 10
    height = 14
    expected = 140
    #invoke
    actual = areas.rectangle(width, height)
    #analyze
    assert actual == expected
    
def rectangle_negative_width():
    #setup
    width = -1
    height = 10
    expected = None
    #invoke
    actual = areas.rectangle(width, height)
    #analyze
    assert actual == expected

def rectangle_negative_height():
    #setup
    width = 10
    height = -1
    expected = None
    #invoke
    actual = areas.rectangle(width, height)
    #analyze
    assert actual == expected

def square_negative_length():
    #setup
    length = -1
    expected = None
    #invoke
    actual = areas.square(length)
    #analyze
    assert actual == expected

def test_triangle_8_10():
    #setup
    base = 8
    height = 10
    expected = 40
    #invoke
    actual = areas.triangle(base, height)
    #analyze
    assert actual == expected

def triangle_negative_base():
    #setup
    base = -1
    height = 10
    expected = None
    #invoke
    actual = areas.triangle(base, height)
    #analyze
    assert actual == expected

def triangle_negative_height():
    #setup
    base = 10
    height = -1
    expected = None
    #invoke
    actual = areas.triangle(base, height)
    #analyze
    assert actual == expected