# Write text in turtle canvas

# turtle.write()
# style = (fontname, fontsize, fonttype)
# fonttype = 'normal', 'bold', 'italic'
# align = 'left', 'center', 'right'
# move = True / False (for underline)

import turtle

t = turtle.Turtle()
t.penup()
t.goto(205, -50)
t.pendown()
t.color('black')
style = ('Roboto', 50, 'bold')
t.write('Terima Kasih', font=style, align='right', move=True)
t.hideturtle()
turtle.color("red")
turtle.begin_fill()
turtle.left(50)
turtle.forward(100)
turtle.circle(40, 180)
turtle.left(260)
turtle.circle(40, 180)
turtle.forward(100)
turtle.end_fill()
turtle.done()
