from Algorithms import dda_algrithm


def angulo(n):
    alfa = 180 * (n - 2)
    return alfa//n


def listar(puntos,funcion):
    fin = len(puntos)-1
    coordenadas = []
    for i in range(fin):
        #DDA
        n = funcion(puntos[i][0],puntos[i][1],puntos[i+1][0],puntos[i+1][1])
        coordenadas.append(n)
    n = funcion(puntos[fin][0],puntos[fin][1],puntos[0][0],puntos[0][1])
    coordenadas.append(n)
    return coordenadas

if __name__ == '__main__':
    a = angulo(5)
    print (a)
