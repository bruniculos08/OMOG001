import random as random
from math import *
import matplotlib.pyplot as plt
import numpy as np

# Fazendo código para gerar curva de Bezier de grau 2 (3 pontos) em 3 dimensões (mas plotando em 2 por enquanto):

def quad_bezier_funcs(p0, p1, p2):
    x0, y0, z0 = p0[0], p0[1], p0[2]
    x1, y1, z1 = p1[0], p1[1], p1[2]
    x2, y2, z2 = p2[0], p2[1], p2[2]
    
    def xf(u):
        return ((1-u)**2)*x0 + 2*u*(1-u)*x1 + (u**2)*x2
    
    def yf(u):
        return ((1-u)**2)*y0 + 2*u*(1-u)*y1 + (u**2)*y2
    
    def zf(u):
        return ((1-u)**2)*z0 + 2*u*(1-u)*z1 + (u**2)*z2

    return xf, yf, zf

def line_funcs(pA, pB):

    def x_line(u):
        return (pB[0]-pA[0])*u + pA[0]
    
    def y_line(u):
        return (pB[1]-pA[1])*u + pA[1]
    
    def z_line(u):
        return (pB[2]-pA[2])*u + pA[2]
    
    return x_line, y_line, z_line

    
# A grande beleza de uma curva de Bezier é ela terminar dentro do polígono
if __name__ == '__main__':
    p0 = [0, 0, 0]
    p1 = [1, 1, 0]
    p2 = [3, 1.5, 0]


    extra_interval = 0
    U = np.linspace(0-extra_interval, 1+extra_interval, 1000)

    xf, yf, zf = quad_bezier_funcs(p0, p1, p2)
    X = [xf(ui) for ui in U]
    Y = [yf(ui) for ui in U]
    Z = [zf(ui) for ui in U]

    plt.xlim(-0.5,4)
    plt.ylim(0,2)

    plt.plot(X, Y, label = "blue")

    # Linha de p0 até p1:
    U = np.linspace(0, 1, 1000)
    x_line_func, y_line_func, z_line_func = line_funcs(p0, p1)
    X = [x_line_func(ui) for ui in U]
    Y = [y_line_func(ui) for ui in U]
    Z = [z_line_func(ui) for ui in U]

    plt.plot(X, Y, label = "green")

    # Linha de p1 até p2:
    U = np.linspace(0, 1, 1000)
    x_line_func, y_line_func, z_line_func = line_funcs(p1, p2)
    X = [x_line_func(ui) for ui in U]
    Y = [y_line_func(ui) for ui in U]
    Z = [z_line_func(ui) for ui in U]

    plt.plot(X, Y, label = "orange")



    plt.savefig("Exemplo01-Bezier.png")
    plt.show()
    plt.close()