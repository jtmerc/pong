# Import modules
import turtle

# First, we will create screen
screen_1 = turtle.Screen()
screen_1.title("Ping-Pong Game")
screen_1.bgcolor("Black")
screen_1.setup(width=1050, height=650)

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("White")
left_paddle.shapesize(stretch_wid=6, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-400, 0)

# Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("White")
right_paddle.shapesize(stretch_wid=6, stretch_len=2)
right_paddle.penup()
right_paddle.goto(400, 0)

# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(175)
hit_ball.shape("circle")
hit_ball.color("White")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# score
left_player = 0
right_player = 0

# Display of score
sketch_1 = turtle.Turtle()
sketch_1.speed(0)
sketch_1.color("white")
sketch_1.penup()
sketch_1.hideturtle()
sketch_1.goto(0, 260)
sketch_1.write("Left Player : 0    Right Player: 0",
               align="center", font=("Courier", 24, "normal"))


# Implementing the functions for moving paddle vertically
def paddle_l_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def paddle_l_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)


def paddle_r_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)


def paddle_r_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)


# Then, binding the keys for moving the paddles up and down.
screen_1.listen()
screen_1.onkeypress(paddle_l_up, "w")
screen_1.onkeypress(paddle_l_down, "s")
screen_1.onkeypress(paddle_r_up, "Up")
screen_1.onkeypress(paddle_r_down, "Down")

while True:
    screen_1.update()

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Check all the borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch_1.clear()
        sketch_1.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch_1.clear()
        sketch_1.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

        # Collision of ball and paddles
    if (hit_ball.xcor() > 360 and
        hit_ball.xcor() < 370) and (hit_ball.ycor() < right_paddle.ycor() + 60 and
                                    hit_ball.ycor() > right_paddle.ycor() - 60):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (hit_ball.xcor() < -360 and
        hit_ball.xcor() > -370) and (hit_ball.ycor() < left_paddle.ycor() + 60 and
                                     hit_ball.ycor() > left_paddle.ycor() - 60):
        hit_ball.setx(-360)
        hit_ball.dx *= -1