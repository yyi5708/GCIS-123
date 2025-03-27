import turtle

PIXEL_SIZE = (30)
ROWS = (20)
COLUMNS = (20)

def init():
    x = PIXEL_SIZE * COLUMNS / 2
    y = PIXEL_SIZE * ROWS / 2
    turtle.reset()
    turtle.speed(0)
    turtle.up()
    turtle.goto(-x, y)
    turtle.pencolor("Black")
    turtle.fillcolor("White")

def pixel(pixel_color):
    turtle.pencolor("black")
    turtle.fillcolor(pixel_color)
    turtle.begin_fill()
    turtle.down()
    turns = 4
    while turns != 0:
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
        turns = turns - 1
    
    turtle.end_fill()
    turtle.up()
    turtle.forward(PIXEL_SIZE)

def move(column, row):
    top_left_x = PIXEL_SIZE * COLUMNS / 2 * -1
    top_left_y = PIXEL_SIZE * ROWS / 2
    x = top_left_x + (column * PIXEL_SIZE)
    y = top_left_y + (row * PIXEL_SIZE)
    turtle.goto(x, y)

def draw_row(row, column, n, color="Red"):
    move(column, row)
    #while number > 0:
        #pixels(color)
        #number = number - 1
    for _ in range(n):
        pixel(color)

def draw_square(row, column, size, color="Red"):
    for _ in range(size):
        draw_row(row, column, size, color)
        row = row + 1

def draw_rectangle(row, column, height, width, color="Red"):
    for _ in range(height):
        draw_row(row, column, width, color)
        row = row + 1

def main():
    init()
    #pixel("Red")
    #draw_row(1, 1, 10)
    #draw_square(-5, -5, 10)
    draw_rectangle(-10, -10, 5, 10)
    input("Press enter to exit: ")

if __name__ == "__main__":
    main()
