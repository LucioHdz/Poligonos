import turtle
import Mates
if __name__ == '__main__':
    points = []
    size = 5
    lados = int(input('Lados: '))
    angulo = Mates.angulo(lados)
    angulo = 180-angulo
    window = turtle.Screen()
    window.bgcolor('black')

    pen = turtle.Turtle()
    # pen.penup()
    # pen.goto(0,-(window.window_height()//2-10))
    # pen.pendown()
    # pen.color("#00a4f5")

    for i in range (lados):
        points.append([int(pen.pos()[0]),int(pen.pos()[1])])
        pen.forward(size)
        pen.left(angulo)
    print(points)

    turtle.mainloop()