import turtle

turtle.speed(20)

def get_side_length():
    """
    this program is to get the side length of the plus sign from the user
    :return: returns the side length
    """
    side_length = float(input("what is the side length?"))
    return side_length

def get_color():
    """
    this program is to get the plus sign color
    :return: returns the color
    """
    plus_color = input("what color should your plus sign be?")
    return plus_color

def draw_plus_sign(side_length):
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
    turtle.end_fill()


def recenter():
    """
    this program recenters turtle to 0,0
    :return: returns recenter
    """
    turtle.penup()
    turtle.goto(0,0)
    return recenter()


def main():
    side_length = get_side_length()
    plus_color = get_color()

    turtle.color(plus_color)
    turtle.begin_fill()
    draw_plus_sign(side_length)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(side_length)
    turtle.forward(side_length)
    turtle.forward(side_length)
    turtle.left(90)
    turtle.pendown()
    turtle.begin_fill()
    draw_plus_sign(side_length)
    turtle.end_fill

    recenter()
    turtle.left(90)
    turtle.forward(side_length)
    turtle.forward(side_length)
    turtle.forward(side_length)
    turtle.pendown()
    turtle.begin_fill()
    draw_plus_sign(side_length)
    turtle.end_fill()

    recenter()
    turtle.right(90)
    turtle.forward(side_length)
    turtle.forward(side_length)
    turtle.forward(side_length)
    turtle.left(180)
    turtle.pendown()
    turtle.begin_fill()
    draw_plus_sign(side_length)
    turtle.end_fill()
    recenter()
    turtle.right(180)
    turtle.forward(side_length)
    turtle.forward(side_length)
    turtle.forward(side_length)
    turtle.right(90)
    turtle.pendown()
    turtle.begin_fill()
    draw_plus_sign(side_length)
    turtle.end_fill()
    turtle.exitonclick()

main()