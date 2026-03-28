import turtle

turtle.speed(0)

def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()

def draw_square(x, y, size, color1, color2):
    draw_triangle(x, y+size, x+size, y+size, x+size, y, color1)
    draw_triangle(x, y+size, x+size, y, x, y, color2)

size = 60

draw_square(0, 0, size, "blue", "darkblue")
draw_square(60, 0, size, "darkblue", "red")
draw_square(120, 0, size, "red", "blue")
draw_square(180, 0, size, "blue", "red")
draw_square(240, 0, size, "red", "blue")

draw_square(0, 60, size, "blue", "red")
draw_square(60, 60, size, "red", "blue")
draw_square(120, 60, size, "blue", "red")
draw_square(180, 60, size, "red", "blue")
draw_square(240, 60, size, "blue", "red")

turtle.hideturtle()
turtle.done()