import turtle
import Mates
from Algorithms import * 

origen_x = -100
origen_y = -100
square_size = 10
def square(x,y,pen):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    for i in range(4):
        pen.forward(square_size)
        pen.right(90)

def print_squares(x,y,pen):
    for i in range(len(x)):
            x_v = x[i] * square_size + origen_x
            y_v = y[i] * square_size + origen_y
            square(x_v,y_v,pen)

def get_points(pen,lados):
    points = []
    for i in range (lados):
        points.append([int(pen.pos()[0]),int(pen.pos()[1])])
        pen.forward(size)
        pen.left(angulo)
    return points

if __name__ == '__main__':
    size = 10
    lados = int(input('Lados: '))
    angulo = Mates.angulo(lados)
    angulo = 180-angulo

    algoritmo = int(input('''
    1)DDA
    2)Bresenham
    -->'''))
    window = turtle.Screen()
    window.bgcolor('black')

    pen = turtle.Turtle()
    # pen.penup()
    # pen.goto(0,-(window.window_height()//2-10))
    # pen.pendown()

    points = get_points(pen,lados)
    print(points)
    if algoritmo == 1:
        coord = Mates.listar(points,dda_algrithm)
    else:
        coord = Mates.listar(points,bresenham_algrithm)
    pen.color("#00a4f5")
    
    print(coord)
    for c in coord:
        x_vars = c[0]
        y_vars = c[1]
        print_squares(x_vars,y_vars,pen)

    turtle.mainloop()
