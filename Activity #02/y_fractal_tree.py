from turtle import *

speed("fastest")

rt(-90)

angle = 30


def y(size, level):
    if level > 0:
        colormode(255)

        pencolor(0, 255 // level, 0)

        fd(size)

        rt(angle)

        y(0.8 * size, level - 1)

        pencolor(0, 255 // level, 0)

        lt(2 * angle)

        y(0.8 * size, level - 1)

        pencolor(0, 255 // level, 0)

        rt(angle)

        fd(-size)


y(80, 7)
