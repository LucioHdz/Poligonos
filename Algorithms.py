def dda_algrithm(x,y,x2,y2):
    """Algoritmo de trazos DDA
    Args:
        x (integer): posicion x coordenada 1
        y (integer): posicion y coordenada 1
        x2 (integer): posicion x coordenada 2
        y2 (integer): posicion y coordenada 2
    Returns:
        List(int): Listas x,y coordinadas
    """
    dx = abs(x2-x)
    dy = abs(y2-y)
    steps = 0
    if dx>dy:
        steps = dx
    else:
        steps = dy

    increment_x = dx / steps     
    increment_y = dy / steps

    p1 = x
    p2 = y
    x_vars=[p1]
    y_vars=[p2]
    for i in range(steps):
        if x2 < x:
            p1 -= increment_x
        else:
            p1 += increment_x
        n = round(p1)
        x_vars.append(n)
        if y2>y:
            p2 += increment_y
        else:
            p2 -= increment_y 
        n = round(p2)
        y_vars.append(n)
    return x_vars,y_vars


def bresenham_algrithm(x,y,x2,y2):
    """Algoritmo de trazos Bresenham
    Args:
        x (integer): posicion x coordenada 1
        y (integer): posicion y coordenada 1
        x2 (integer): posicion x coordenada 2
        y2 (integer): posicion y coordenada 2
    Returns:
        List(int): Listas x,y coordinadas
    """
    dx = abs(x2 -x)
    dy = abs(y2 -y)
    p = 2 * dy -dx
    x_vars=[]
    y_vars=[]
    if dx !=0:
        if x<x2:
            while x <= x2:
                x_vars.append(x)
                y_vars.append(y)   
                x += 1
                if p<0:
                    p = p + 2 * dy
                else:
                    p = p + (2 * dy) - (2 * dx)
                    if y< y2:
                        y += 1
                    elif y>y2:
                        y -= 1
        else:
            while x >= x2:
                x_vars.append(x)
                y_vars.append(y)   
                x -= 1
                if p<0:
                    p = p + 2 * dy
                else:
                    p = p + (2 * dy) - (2 * dx)
                    if y< y2:
                        y += 1
                    elif y>y2:
                        y -= 1
    else:
        if y<=y2:
            while y <= y2:
                x_vars.append(x)
                y_vars.append(y)
                if p<0:
                    p = p + 2 * dy
                else:
                    p = p + (2 * dy) - (2 * dx)
                    y += 1
        else:
            while y >= y2:
                x_vars.append(x)
                y_vars.append(y)
                if p<0:
                    p = p + 2 * dy
                else:
                    p = p + (2 * dy) - (2 * dx)
                    y -= 1
    return x_vars,y_vars

if __name__ == '__main__':
    print(bresenham_algrithm(0,0,10,0))
    print(bresenham_algrithm(10,0,17,7))
    print(bresenham_algrithm(17,7,17,17))
    print(bresenham_algrithm(17,17,9,24))
    print(bresenham_algrithm(9,24,0,24))
    print(bresenham_algrithm(0,24,-7,17))
    print(bresenham_algrithm(-7,17,-7,7))
    print(bresenham_algrithm(-7,7,0,0))