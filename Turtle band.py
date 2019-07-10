import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
sides = eval( input("Enter a number of sides between 2 and 6: ") )
colors = eval( input("what color do you want it: ") )
for x in range(360):
    print("x value:" + str(x) +  "  side value:" + str(sides) + " remainder of x / side : " +  str(x%sides) )
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
    t.left(90)