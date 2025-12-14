import turtle

turtle.bgcolor("black")
turtle.speed(3)

# Draw red square
turtle.color("red")
turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
turtle.begin_fill()

turtle.forward(80)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(80)
turtle.end_fill()


turtle.color("white")
turtle.pensize(2)
turtle.penup()
turtle.goto(240,-200)
turtle.pendown()

for _ in range(30):       
    turtle.forward(7)
    turtle.left(1)
    turtle.forward(7)
    turtle.left(1)


turtle.shape("circle")
turtle.color("white")
turtle.shapesize(1.2)
turtle.penup()
turtle.clone()
number = 1
turtle.shapesize(number)
turtle.shape("square")
turtle.stamp()
turtle.fillcolor("")  # Make it unfilled
for _ in range(40):
    turtle.pendown()
    turtle.clone()
    turtle.right(30)
    number += 0.5
    turtle.penup()
    turtle.shapesize(number)






turtle.done()
