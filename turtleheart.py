import turtle

wn = turtle.Screen()
elan = turtle.Turtle()
elan.color("blue")
rus = turtle.Turtle()
rus.color("red")
mag = turtle.Turtle()
mag.color("purple")
rag = turtle.Turtle()
rag.color("violet")
distance = 20
angle = 50
for _ in range(8):
    elan.forward(distance)
    elan.right(angle)
    rus.forward(distance)
    rus.left(angle)
    mag.forward(distance + 2)
    mag.right(angle + 3)
    rag.forward(distance + 2)
    rag.left(angle + 3)
    distance = distance + 5
    angle = angle - 5
wn.exitonclick()