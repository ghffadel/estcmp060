from playsound import playsound
import turtle


class Paddle:
    # initialize the values
    def __init__(self, player):
        self.paddle = turtle.Turtle()
        self.score = 0
        self.x_position = -350 if player == 1 else 350

    # draw paddle
    def draw_paddle(self):
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(self.x_position, 0)

    # move up the paddle
    def up(self):
        y = min(self.paddle.ycor() + 30, 250)
        self.paddle.sety(y)

    # move down the paddle
    def down(self):
        y = max(self.paddle.ycor() - 30, -250)
        self.paddle.sety(y)
    
    # check collision between the ball and the paddle
    def check_collision(self):
        if abs(self.x_position) - 10 < abs(ball.xcor()) < abs(self.x_position) + 10 and \
                self.paddle.ycor() - 60 < ball.ycor() < self.paddle.ycor() + 60:
            ball.setx(self.x_position + (10 if self.x_position < 0 else -10))

            if self.paddle.ycor() - 30 <= ball.ycor() <= self.paddle.ycor() + 30:
                ball.dx *= -1

            else:
                ball.dx *= -0.5

            playsound("bounce.wav")

# default values for head-up display
def draw_head_display():
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()


# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# draw ball
ball = turtle.Turtle()
ball.speed(5)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# head-up display
hud = turtle.Turtle()
draw_head_display()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

# initialize the paddles
paddle_1 = Paddle(1)
paddle_1.draw_paddle()
paddle_2 = Paddle(2)
paddle_2.draw_paddle()

# keyboard
screen.listen()
screen.onkeypress(paddle_1.up, "w")
screen.onkeypress(paddle_1.down, "s")
screen.onkeypress(paddle_2.up, "Up")
screen.onkeypress(paddle_2.down, "Down")

while True:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with upper wall or lower wall
    if abs(ball.ycor()) > 290:
        if ball.ycor() > 290:
            ball.sety(290)

        else:
            ball.sety(-290)

        ball.dy *= -1
        ball.speed(5)
        playsound("bounce.wav")

    # collision with left wall or right wall
    if abs(ball.xcor()) > 390:
        if ball.xcor() > 390:
            paddle_1.score += 1

        else:
            paddle_2.score += 1

        hud.clear()
        hud.write("%d : %d" % (paddle_1.score, paddle_2.score), align="center", font=("Press Start 2P", 24, "normal"))
        playsound("258020__kodack__arcade-bleep-sound.wav")
        ball.goto(0, 0)
        ball.dx *= -1
        ball.speed(5)
    
    # check collision in the 2 balls
    paddle_1.check_collision()
    paddle_2.check_collision()
    
    # ends the game if a player reach 10 points
    if paddle_1.score == 10 or paddle_2.score == 10:
        screen.reset()
        hud = turtle.Turtle()
        draw_head_display()
        hud.goto(0, 50)

        if paddle_1.score == 10:
            hud.write("PLAYER 1 WINS!", align="center", font=("Press Start 2P", 24, "normal"))

        else:
            hud.write("PLAYER 2 WINS!", align="center", font=("Press Start 2P", 24, "normal"))

        hud.goto(0, 10)
        hud.write("\nPress Enter to leave the game", align="center", font=("Press Start 2P", 24, "normal"))

        screen.onkeypress(screen.bye, "Return")
        screen.listen()
