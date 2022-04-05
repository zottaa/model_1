from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import queue

#8 вариант
#cos(2t)^2 + sin(2t)

#T поступление (1, 15) T обработки (1, 19)


def det_dx(f, N):
    dt = 0.01
    t = symbols('t')
    f = lambdify(t, f)
    t = 0
    _det_dx = []
    count = 0
    while count != N + 1:
        _det_dx.append((f(t + dt) - f(t)) / dt)
        t += dt
        count += 1
    return _det_dx


def model():
    N = 0
    t_wait_queue = 0
    t_wait_pc_1 = 0
    t_wait_pc_2 = 0
    t_in_system = 0
    pc_1_is_busy = False
    pc_2_is_busy = False
    channel_is_busy = False
    t_input_end = -1
    pc_1_end = -1
    pc_2_end = -1
    t_input = -1
    t_handle = -1
    simulation_time = 0
    _queue = queue.Queue()
    while N != 1000:
        if _queue.empty() is False:
            t_wait_queue += 1
        if pc_1_is_busy is False:
            t_wait_pc_1 += 1
        if pc_2_is_busy is False:
            t_wait_pc_2 += 1
        if pc_1_is_busy is True or pc_2_is_busy is True:
            t_in_system += 1
        if simulation_time == pc_1_end:
            N += 1
            pc_1_is_busy = False
        if simulation_time == pc_2_end:
            N += 1
            pc_2_is_busy = False
        if simulation_time == t_input_end and simulation_time != 0:
            channel_is_busy = False
            if pc_1_is_busy is False:
                pc_1_end = simulation_time + t_handle
                pc_1_is_busy = True
            elif pc_2_is_busy is False:
                pc_2_end = simulation_time + t_handle
                pc_2_is_busy = True
            else:
                _queue.put(t_handle)
        if pc_1_is_busy is False and _queue.empty() is False:
            pc_1_end = simulation_time + _queue.get()
            pc_1_is_busy = True
        if pc_2_is_busy is False and _queue.empty() is False:
            pc_2_end = simulation_time + _queue.get()
            pc_2_is_busy = True
        if channel_is_busy is False:
            t_input = randint(1, 15)
            t_handle = randint(1, 19)
            t_input_end = simulation_time + t_input
            channel_is_busy = True
        simulation_time += 1
    print(50*"*")
    return t_wait_queue, t_wait_pc_1, t_wait_pc_2, t_in_system, simulation_time


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
    t_average_wait_queue, t_pc_1_average_p, t_pc_2_average_p, t_average_stay_in_system, simulation_time = 0, 0, 0, 0, 0
    for i in range(1, 101):
        print("Эксперимент №%d" % i)
        t_wait_queue, t_wait_pc_1, t_wait_pc_2, t_in_system, simulation_time = model()
        t_wait_pc = t_wait_pc_1 + t_wait_pc_2
        t_average_wait_queue += (t_wait_queue / 1000)
        t_pc_1_average_p += (t_wait_pc_1 / simulation_time)
        t_pc_2_average_p += (t_wait_pc_2 / simulation_time)
        t_average_stay_in_system += (t_in_system / 1000)
        print("Среднее время пребывания в системе = %.3f сек" % (t_in_system / 1000))
        print("Среднее время ожидания в очереди = %.3f сек" % (t_wait_queue / 1000))
        print("Вероятность простоя ПК1 = %.3f" % (t_wait_pc_1 / simulation_time))
        print("Верояность простоя ПК2 = %.3f" % (t_wait_pc_2 / simulation_time))
    print("\n" + ("*" * 50) + "\n")
    print("Результаты после 100 экспериментов")
    print("Среднее время пребывания в системе = %.3f сек" % (t_average_stay_in_system / 100))
    print("Среднее время ожидания в очереди = %.3f сек" % (t_average_wait_queue / 100))
    print("Вероятность простоя ПК1 = %.3f" % (t_pc_1_average_p / 100))
    print("Вероятность проятоя ПК2 = %.3f" % (t_pc_2_average_p / 100))


main()