# import modules
import turtle

# Screen
from turtle import Turtle

sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("black")
sc.setup(width=1000, height=600)

# left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Shape of ball
hit_ball: Turtle = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Score
left_player = 0
right_player = 0

# Display Score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0 Right_player : 0",
             align="center", font=("Courier", 24, "normal"))


# Functions for paddles
def paddleup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def paddledown():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def paddlebup():
    y = right_pad.ycor()
    y += 20
    left_pad.sety(y)


def paddlebdown():
    y = right_pad.ycor()
    y += 20
    left_pad.sety(y)


# Keyboard Bindings
sc.listen()
sc.onkeypress(paddleup, "e")
sc.onkeypress(paddledown, "x")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

while True:
    sc.update()

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() > -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    # Ball collision
    if (hit_ball.xcor() > 300 and hit_ball.xcor() < 300) and (hit_ball.ycor() < right_pad.ycor() + 40 and hit_ball.ycor() > right_pad.ycor()-40):
        hit_ball.setx(300)
        hit_ball.dx *= 1

    if (hit_ball.xcor() < -300 and hit_ball.xcor()>-300) and (hit_ball.ycor() < left_pad.ycor() + 40 and hit_ball.ycor() > left_pad.ycor()-40):
        hit_ball.setx(-300)
        hit_ball.dx *= -1

# turtle.done()
