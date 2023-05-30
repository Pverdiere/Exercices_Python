import turtle

turtle.speed(8)

# The square
turtle.penup()
turtle.goto(-900,0)
turtle.pendown()
for i in range(4) :
    turtle.forward(100)
    turtle.left(90)
turtle.penup()

# pentagone

turtle.goto(-700,0)
turtle.pendown()
for i in range(5) :
    turtle.forward(100)
    turtle.left(72)
turtle.penup()

# ship

turtle.goto(-500,0)
turtle.pendown()
for i in range(3) :
    turtle.forward(200)
    turtle.left(180 - 60)
turtle.penup()
turtle.forward(100)
turtle.left(90)
turtle.pendown()
turtle.forward(172)
turtle.right(90)
turtle.penup()
turtle.goto(-500,-5)
turtle.pendown()
turtle.forward(200)
turtle.right(180 - 45)
turtle.forward(50)
turtle.right(45)
turtle.forward(130)
turtle.right(45)
turtle.forward(50)

turtle.done()