from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from queue import Queue

#8 вариант
#cos(2t)^2 + sin(2t)

#T поступление (1, 15) T обработки (1, 19)

class Computer:
    def __init__(self):
        self.isBusy = False

    def changeCondition(self):
        if self.isBusy is True:
            self.isBusy = False
        else:
            self.isBusy = True



def det_dx(f, N):
    dt = 0.01
    t = symbols('t')
    f = lambdify(t, f)
    t = 0
    det_dx = []
    count = 0
    while count != N + 1:
        det_dx.append((f(t + dt) - f(t)) / dt)
        t += dt
        count += 1
    return det_dx


def model():
    pass
    N = 0
    pc_1 = Computer()
    pc_2 = Computer()
    t = 0
    queue = Queue()
    while N != 1000:
        Tpost = randint(1, 15)
        Tobr = randint(1, 19)



        t += 1




def main():
    #1
    N = 5000
    x = np.linspace(0, 0.01 * N, N + 1)
    t = symbols('t')
    f = cos(2*t) ** 2 + sin(2 * t)
    det_dx_ = det_dx(f, N)
    dx = f.diff()
    f = lambdify(t, f)
    dx = lambdify(t, dx)
    plt.plot(x, f(x), label='f(t)')
    plt.plot(x, dx(x), label="f'(t)")
    plt.plot(x, det_dx_, label="det f'(t)")
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('1')
    plt.legend()
    plt.show()

    #2



if __name__ == '__main__':
    main()