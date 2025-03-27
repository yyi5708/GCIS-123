import turtle

DEFAULT_SIZE = 50

def draw_square(x, y, size):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)

def draw_circle(x, y, radius):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.circle(radius)

def draw_triangle(x, y, size):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)

def draw_rectangle(x, y, length, width):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width) 
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)

def draw_pentagon(x, y, size):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.forward(size)
    turtle.right(72)
    turtle.forward(size)
    turtle.right(72)
    turtle.forward(size)
    turtle.right(72)
    turtle.forward(size)
    turtle.right(72)
    turtle.forward(size)

def main():
    draw_square(0,0,DEFAULT_SIZE)
    draw_triangle(100,100,DEFAULT_SIZE)
    draw_rectangle(-250,-250,DEFAULT_SIZE,100)
    draw_pentagon(250,250,DEFAULT_SIZE)
    draw_circle(-100,-100,DEFAULT_SIZE)
    input("exit?")

main()

#DONE.