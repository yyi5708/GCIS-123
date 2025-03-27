import turtle
import pixart

def assertle(pen_color, fill_color):
    assert turtle.speed() == 0
    assert turtle.xcor() == -300
    assert turtle.ycor() == 300
    assert turtle.isdown() == False
    assert turtle.pencolor() == "Black"
    assert turtle.fillcolor() == "White"

def test_init():
    #setup
    pixart.init()
    #invoke
    pixart.init()
    #analyze
    assertle("Black", "White")

def test_pixel():
    #setup
    pixart.init()
    #invoke
    pixart.pixel("Red")
    #analyze
    assertle("Red", "Red")

def test_move():
    #setup
    COLUMNS = 20
    ROWS = 20
    #invoke
    pixart.move(COLUMNS,ROWS)
    #analyze
    assertle("Black", "White")

def test_row():
    #setup
    pixart.init()
    row = 1
    column = 1
    n = 10
    #invoke
    x = pixart.draw_row(row, column, n)
    #analyze
    return x

def test_square():
    #setup
    pixart.init()
    row = -5
    column = -5
    size = 10
    #invoke
    x = pixart.draw_square(row, column, size)
    #analyze
    return x

def test_rectangle():
    #setup
    pixart.init()
    row = -10
    column = -10
    height = 5
    width = 10
    #invoke
    x = pixart.draw_rectangle(row, column, height, width)
    #analyze
    return x