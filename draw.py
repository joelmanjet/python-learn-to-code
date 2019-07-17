import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("white")
t.width(10)
def up():
    t.forward(50)
def left():
    t.left(90)
def right():
    t.right(90)
turtle.onkeypress(up,"Up")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()