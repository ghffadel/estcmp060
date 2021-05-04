from math import pi
import turtle


def generate_plot(n):
    a, b = 0, 1
    square_a, square_b = a, b

    plot.pencolor("blue")

    plot.forward(b * scale)
    plot.left(90)
    plot.forward(b * scale)
    plot.left(90)
    plot.forward(b * scale)
    plot.left(90)
    plot.forward(b * scale)

    square_a, square_b = square_b, square_a + square_b

    for i in range(1, n):
        plot.backward(square_a * scale)
        plot.right(90)
        plot.forward(square_b * scale)
        plot.left(90)
        plot.forward(square_b * scale)
        plot.left(90)
        plot.forward(square_b * scale)

        square_a, square_b = square_b, square_a + square_b

    plot.penup()
    plot.setposition(scale, 0)
    plot.seth(0)
    plot.pendown()

    plot.pencolor("red")

    plot.left(90)

    for i in range(n):
        print(b)
        fwrd = (pi * b * scale / 2) / 90
        for j in range(90):
            plot.forward(fwrd)
            plot.left(1)
        a, b = b, a + b


iterations = int(input("Enter the number of iterations: "))
scale = 1

if iterations > 0:
    print("Fibonacci series for", iterations, "elements:")
    plot = turtle.Turtle()
    plot.speed(100)
    generate_plot(iterations)
    turtle.done()
else:
    print("Number of iterations must be bigger than 0")
