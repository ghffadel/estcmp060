import turtle

screen = turtle.Screen()
plot = turtle.Turtle()


def triangle(x, y):
    plot.penup()
    plot.goto(x, y)
    plot.pendown()

    for i in range(3):
        plot.forward(100)
        plot.left(120)
        plot.forward(100)


turtle.onscreenclick(triangle, 1)
turtle.listen()
turtle.done()
