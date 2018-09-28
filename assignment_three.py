import turtle

side_length = float(input("what is the side length?"))
turtle.speed(10)


def PlusSign():
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
PlusSign()

turtle.penup()
turtle.forward(side_length)
turtle.forward(side_length)
turtle.left(90)
turtle.forward(side_length)
turtle.pendown()
PlusSign()








turtle.exitonclick()
