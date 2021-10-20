import turtle

def position(x,y,c):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(c)
    turtle.begin_fill()
    
def draw_rect(s1,s2):
    for i in range(2):
        turtle.forward(s1)
        turtle.right(90)
        turtle.forward(s2)
        turtle.right(90)
    
    turtle.end_fill()

#Student 1

#Call the function "position" and pass the paremeters as 10, -10, "red"

for i in range(3):
    turtle.forward(100)
    turtle.left(120)
    
turtle.end_fill()

#Call the function "position" and pass the paremeters as 85, -40, "blue"

#Call the function "draw_rect" and pass the paremeters as 40, 150


#Student 2

#Call the function "position" and pass the paremeters as 10, -10, "green"

#Call the function "draw_rect" and pass the paremeters as 100, 150

#Call the function "position" and pass the paremeters as -5, -40, "blue"

#Call the function "draw_rect" and pass the paremeters as 40, 150

turtle.ht()
