import turtle
import time 

print("Loading, please wait...")
time.sleep(1.5)

frame = turtle.Turtle()
bird = turtle.Turtle() 
screen = turtle.Screen()
bullet1 = turtle.Turtle()
bullet2 = turtle.Turtle()
bullet3 = turtle.Turtle()
bullet4 = turtle.Turtle()
bullet5 = turtle.Turtle()
bulletSpeed = 2
score = 0 
highScore = 0
txt = turtle.Turtle()
txt2 = turtle.Turtle()

frame.hideturtle()
frame.speed(0)
frame.setheading(180)
frame.penup()
frame.pencolor("light green")
frame.pensize(3)
frame.goto(300, 300)
frame.pendown()
for i in range(4):
    frame.forward(600)
    frame.left(90)

screen.delay(0)
screen.bgcolor("black")
screen.setup(width=640, height=640)
screen.title("Dodging Bird")

bird.penup()
bird.setheading(90)
bird.goto(x= -200, y= 200)
bird.shapesize(stretch_wid=2, stretch_len=1.5) 
bird.speed(0)

txt.penup()
txt.hideturtle()
txt.color("red")

txt2.penup()
txt2.hideturtle()
txt2.speed(0)
txt2.color("cyan")
txt2.goto(x = 0, y = -290)
txt2.write("Score: 0 - High Score: 0", align = "center", font = ("courier", 25, "normal"))

bullet1.penup()
bullet1.goto(400, 200)
bullet1.shape("circle")
bullet1.color("white")
bullet1.shapesize(stretch_wid= 0.7, stretch_len= 0.7)
bullet1.setheading(180)
bullet1.showturtle()
bullet1.speed(0)

bullet2.penup()
bullet2.goto(600, 100)
bullet2.shape("circle")
bullet2.color("white")
bullet2.shapesize(stretch_wid= 0.7, stretch_len= 0.7)
bullet2.setheading(180)
bullet2.showturtle()
bullet2.speed(0)

bullet3.penup()
bullet3.goto(800, -100)
bullet3.shape("circle")
bullet3.color("white")
bullet3.shapesize(stretch_wid= 0.7, stretch_len= 0.7) 
bullet3.setheading(180)
bullet3.showturtle()
bullet3.speed(0)

bullet4.penup()
bullet4.goto(500, -200)
bullet4.shape("circle")
bullet4.color("white")
bullet4.shapesize(stretch_wid= 0.7, stretch_len= 0.7) 
bullet4.setheading(180)
bullet4.showturtle()
bullet4.speed(0)

bullet5.penup()
bullet5.goto(700, 0)
bullet5.shape("circle")
bullet5.color("white")
bullet5.shapesize(stretch_wid= 0.7, stretch_len= 0.7) 
bullet5.setheading(180)
bullet5.showturtle()
bullet5.speed(0)

while True:
    screen.update() 

    bird.color("yellow") 
    bird.shape("square")

    bullet1.forward(bulletSpeed)
    bullet2.forward(bulletSpeed)
    bullet3.forward(bulletSpeed)
    bullet4.forward(bulletSpeed)
    bullet5.forward(bulletSpeed)

    if bullet1.xcor() < -300:
        bullet1.goto(400, 200)
        bullet1.setheading(180)
        bulletSpeed += 0.05
        txt2.clear()
        score += 10
        if score >= highScore:
            highScore = score
        txt2.write("Score: {}    High Score: {}".format(score, highScore), align = "center", font = ("Courier", 24, "normal"))


    if bullet2.xcor() < -300:
        bullet2.goto(600,100)
        bullet2.setheading(180)
        bulletSpeed += 0.05
        txt2.clear()
        score += 10
        if score >= highScore:
            highScore = score
        txt2.write("Score: {}    High Score: {}".format(score, highScore), align = "center", font = ("Courier", 24, "normal"))

    if bullet3.xcor() < -300:
        bullet3.goto(800, -100)
        bullet3.setheading(180)
        bulletSpeed += 0.05
        txt2.clear()
        score += 10
        if score >= highScore:
            highScore = score
        txt2.write("Score: {}    High Score: {}".format(score, highScore), align = "center", font = ("Courier", 24, "normal"))

    if bullet4.xcor() < -300:
        bullet4.goto(500, -200)
        bullet4.setheading(180)
        bulletSpeed += 0.05
        txt2.clear()
        score += 10
        if score >= highScore:
            highScore = score
        txt2.write("Score: {}    High Score: {}".format(score, highScore), align = "center", font = ("Courier", 24, "normal"))

    if bullet5.xcor() < -300:
        bullet5.goto(700, 0)
        bullet5.setheading(180)
        bulletSpeed += 0.05
        txt2.clear()
        score += 10
        if score >= highScore:
            highScore = score
        txt2.write("Score: {}    High Score: {}".format(score, highScore), align = "center", font = ("Courier", 24, "normal"))

    if bird.distance(bullet1) < 30 or bird.distance(bullet2) < 30 or bird.distance(bullet3) < 30 or bird.distance(bullet4) < 30 or bird.distance(bullet5) < 30:
        txt.write("Game Over", align = "center", font=("Courier", 45, "bold"))
        time.sleep(5)
        txt.clear()
        bird.goto(-200, 200)
        bullet1.goto(400, 200)
        bullet1.setheading(180)
        bullet2.goto(600, 100)
        bullet2.setheading(180)
        bullet3.goto(800, -100)
        bullet3.setheading(180)
        bullet4.goto(500, -200)
        bullet4.setheading(180)
        bullet5.goto(700, 0)
        bullet5.setheading(180)
        txt2.clear()
        score = 0
        bulletSpeed = 2
        txt2.write("Score: {}    High Score: {}".format(score, highScore), align = "center", font = ("Courier", 24, "normal"))

    if bird.ycor() < -280 or bird.ycor() > 280:
        txt.write("Game Over", align = "center", font=("Courier", 45, "bold"))
        time.sleep(5)
        txt.clear()
        bird.goto(-200, 200)
        bullet1.goto(400, 200)
        bullet1.setheading(180)
        bullet2.goto(600, 100)
        bullet2.setheading(180)
        bullet3.goto(800, -100)
        bullet3.setheading(180)
        bullet4.goto(500, -200)
        bullet4.setheading(180)
        bullet5.goto(700, 0)
        bullet5.setheading(180)
        txt2.clear()
        score = 0
        bulletSpeed = 2
        txt2.write("Score: {}    High Score: {}".format(score, highScore), align = "center", font = ("Courier", 24, "normal"))

    bird.back(3.5) 

    def up():
        bird.forward(60)

    screen.listen()
    screen.onkey(up, "Up")
