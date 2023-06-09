import turtle
import time
import random
from random import randint

pen = turtle.Turtle()
wn = turtle.Screen()
pen.hideturtle()

# Declaring Variables
score_a = 0
score_b = 0
xx = 0
is_paused = False
no = True
medium = False
hard = False

# Main Game Function

def game():
    global score_a, score_b, xx, medium 
    # Pen
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center",
              font=("Courier", 24, "normal"))

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.color("red")
    paddle_a.shape("square")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("blue")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.shapesize(stretch_wid=1, stretch_len=1)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.1
    ball.dy = -0.1

    # Difficulty Setting
    if medium is True and hard is False:
        ball.dx = 0.182
        ball.dy = -0.182
    else:
        if medium is False and hard is True:
            ball.dx = 0.25
            ball.dy = -0.25

    # Paddle and Game Functions

    def paddle_a_up():
        if not is_paused:
            y = paddle_a.ycor()
            y += 20
            paddle_a.sety(y)

    def paddle_a_down():
        if not is_paused:
            y = paddle_a.ycor()
            y -= 20
            paddle_a.sety(y)

    def paddle_b_up():
        if not is_paused:
            y = paddle_b.ycor()
            y += 20
            paddle_b.sety(y)

    def paddle_b_down():
        if not is_paused:
            y = paddle_b.ycor()
            y -= 20
            paddle_b.sety(y)

    # Exit function

    def exit():
        turtle.Screen().bye()

    # Pause Function
    def toggle_pause():
        global is_paused
        if is_paused == False:
            is_paused = True
        else:
            is_paused = False

    # Border Function

    def border():
        pen.up()
        pen.pensize(5)
        pen.goto(-395, 295)
        pen.color("yellow")
        pen.down()
        for i in range(2):
            pen.forward(785)
            pen.right(90)
            pen.forward(585)
            pen.right(90)

    # Score Function

    def score():
        pen.up()
        pen.clear()
        pen.color("white")
        pen.goto(0, 260)
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))

    # Middle Dashed Line

    def dottedline():
        pen.penup()
        pen.pensize(5)
        pen.color("white")
        pen.fillcolor("white")
        pen.goto(-5, 320)
        pen.right(90)
        for i in range(10):
            pen.begin_fill()
            pen.forward(30)
            pen.pendown()
            pen.forward(30)
            pen.penup()
    border()
    dottedline()

    # Setting The RGB Limit for the Window
    wn.colormode(255)

    # Main Game Loop
    while True:
      if not is_paused:
        wn.update()

        # Setting A Ball Speed
        ball.speed(10)

        # Color Changing Ball
        colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if xx > 1:
            ball.color(colors)
            xx -= 2
        # Moving the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        # Border checking for ball and paddle
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if paddle_a.ycor() > 250:
            paddle_a.sety(250)

        if paddle_a.ycor() < -250:
            paddle_a.sety(-250)

        if paddle_b.ycor() > 250:
            paddle_b.sety(250)

        if paddle_b.ycor() < -250:
            paddle_b.sety(-250)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.left(90)
            score()
            border()
            dottedline()

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.left(90)
            score()
            border()
            dottedline()

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b. ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a. ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
        # Score

        if score_a == 10:
            time.sleep(0.45)
            pen.goto(0, 0)
            pen.write("Player A Wins", align="center",
                      font=("Courier", 24, "normal"))
            wn.bgcolor("red")
            time.sleep(5)
            break

        else:
            if score_b == 10:
                time.sleep(0.45)
                pen.goto(0, 0)
                pen.write("Player B Wins", align="center",
                          font=("Courier", 24, "normal"))
                wn.bgcolor("blue")
                time.sleep(5)
                break

        # Moving the paddle and other keys
        wn.onkeypress(toggle_pause, "space")
        wn.onkeypress(exit, "p")
        wn.onkeypress(paddle_a_up, "w")
        wn.onkeypress(paddle_a_down, "s")
        wn.onkeypress(paddle_b_up, "Up")
        wn.onkeypress(paddle_b_down, "Down")
        wn.listen()
        if xx != 2:
            xx += 4

      else:
        wn.update()

# Button Dimensions
easy_x = -200
easy_y = -50
easy_length = 70
easy_width = 50

medium_x = -50
medium_y = -50
medium_length = 90
medium_width = 50

hard_x = 120
hard_y = -50
hard_length = 70
hard_width = 50

mode = "dark"
# Draw Button Function
xyx = True

def draw_easyButton(pen, message="easy"):
    pen.color("red")
    pen.penup()
    pen.fillcolor("Blue")
    pen.begin_fill()
    pen.goto(easy_x, easy_y)
    pen.goto(easy_x + easy_length, easy_y)
    pen.goto(easy_x + easy_length, easy_y + easy_width)
    pen.goto(easy_x,  easy_y + easy_width)
    pen.goto(easy_x, easy_y)
    pen.end_fill()
    pen.goto(easy_x + 15, easy_y + 15)
    pen.write(message, font=("Arial", 15, "normal"))

def draw_mediumButton(pen, message="medium"):
    pen.color("orange")
    pen.penup()
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.goto(medium_x, medium_y)
    pen.goto(medium_x + medium_length, medium_y)
    pen.goto(medium_x + medium_length, medium_y + medium_width)
    pen.goto(medium_x,  medium_y + medium_width)
    pen.goto(medium_x, medium_y)
    pen.end_fill()
    pen.goto(medium_x + 15, medium_y + 15)
    pen.write(message, font=("Arial", 15, "normal"))

def draw_hardButton(pen, message="hard"):
    pen.color("red")
    pen.penup()
    pen.fillcolor("purple")
    pen.begin_fill()
    pen.goto(hard_x, hard_y)
    pen.goto(hard_x + hard_length, hard_y)
    pen.goto(hard_x + hard_length, hard_y + hard_width)
    pen.goto(hard_x,  hard_y + hard_width)
    pen.goto(hard_x, hard_y)
    pen.end_fill()
    pen.goto(hard_x + 15, hard_y + 15)
    pen.write(message, font=("Arial", 15, "normal"))

# Main Screen Loop

while xyx is True:

    # loading screen
    wn.bgcolor("black")
    pen.color("red")
    pen.penup()
    pen.goto(0, 200)
    pen.write("Welcome to pong, by Jayden and Ethan and Gary",
              align="center", font=("Courier", 20, "normal"))
    pen.penup()
    pen.color("blue")
    pen.goto(0, 100)
    pen.write("Controls for Paddle A is W and S",
              align="center", font=("Courier", 20, "normal"))
    pen.goto(0, 70)
    pen.write("Controls for Paddle B is the Up and Down Arrow",
              align="center", font=("Courier", 20, "normal"))
    pen.goto(0, 40)

    # Setup
    wn.title("Pong by Jayden Xia and Ethan Zhang")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    draw_easyButton(pen)
    draw_mediumButton(pen)
    draw_hardButton(pen)

    # Button Clicking Function
    def button_click(x, y):
        global mode, xyx, medium, hard
        if (medium or hard is False):
            if easy_x <= x <= easy_x + easy_length:
                if easy_y <= y <= easy_y + easy_width:
                    xyx = False
                    pen.clear()
                    game()
            elif medium_x <= x <= medium_x + medium_length: 
                if medium_y <= y <= medium_y + medium_width:
                    xyx = False
                    pen.clear()
                    medium = True
                    game()
            else:
                if hard_x <= x <= hard_x + hard_length:
                    if hard_y <= y <= hard_y + hard_width:
                        xyx = False
                        pen.clear()
                        hard = True
                        game()
        else:
            pass
    wn.onclick(button_click)




