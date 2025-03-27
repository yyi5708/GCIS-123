import turtle
ANGLE = 90

def turtle_state():
    d = turtle.isdown()
    print(d)
    h = turtle.heading()
    print(h)
    x = turtle.xcor()
    print(x)
    y = turtle.ycor()
    print(y)

def square(size, ANGLE, pencolor, fillcolor):
    turtle.up()
    turtle.down()
    turtle.pensize(25)
    turtle.pencolor(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(ANGLE)
    turtle.forward(size)
    turtle.left(ANGLE)
    turtle.forward(size)
    turtle.left(ANGLE)
    turtle.forward(size)
    turtle.left(ANGLE)
    turtle.end_fill()
    turtle.up()

def main():
    turtle_state()
    turtle.bgcolor("Beige")
    square(50, ANGLE, "Black", "Gold")
    square(75, ANGLE, "Red", "Navy")
    square(100, ANGLE, "Aqua", "Teal")
    input("Press enter to end: ")
    turtle_state()

main()