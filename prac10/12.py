import turtle

turtle.speed(0)


def circle():
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()


def rhomb():
    turtle.color("blue")
    turtle.begin_fill()
    turtle.forward(40)
    turtle.right(60)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.right(60)
    turtle.forward(40)
    turtle.end_fill()


def triangle():
    turtle.color("green")
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.end_fill()



turtle.up()
turtle.goto(-300, -300)
turtle.down()

for i in range(15):
    circle()
    rhomb()
    triangle()

    turtle.up()
    turtle.forward(80)
    turtle.down()

turtle.hideturtle()
turtle.done()