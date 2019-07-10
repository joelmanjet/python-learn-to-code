import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors=['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'gray', 'brown', 'aqua']
number_of_circles = int(turtle.numinput("Number of circles", "How many circles in your rosette?", 6))
t.speed(0)
t.width(3)
for x in range(number_of_circles):
    t.pencolor(colors[x%10])
    t.circle(100)
    t.left(360/number_of_circles)