import matplotlib.pyplot as plt
import numpy as np
import random as rand

data = np.array([[-4, 2, -3, 3, 12, 6]], float)  # Вариант 9 - c, d, a, b, N, A
line = True # Лин.Функция = TRUE; Парабола = FALSE
c = data[0][0]
d = data[0][1]
a = data[0][2]
b = data[0][3]
N = data[0][4]
A = data[0][5]

def frange(a_ref, b_ref, jump):
    while a_ref < b_ref:
        yield a_ref
        a_ref += jump
def createPoint_XYT(c_ref, d_ref, a_ref, b_ref, N_ref, A_ref):
    Xi = np.array([], float)
    Yi = np.array([], float)
    Ti = np.array([], float)
    for i in frange(a_ref, b_ref, (b_ref - a_ref) / N_ref):
        err = A_ref * (rand.random() - 0.5)
        Xi = np.append(Xi, i)
        Yi = np.append(Yi, c_ref * Xi[-1] + d_ref) if line == True else np.append(Yi, c_ref * Xi[-1] * Xi[-1] + d_ref)
        Ti = np.append(Ti, Yi[-1] + err)
    res = np.vstack([Xi, Yi, Ti])
    res = np.around(res, decimals=1)
    print("\nРаспределение points\n", res, "\n")
    return res

def mnk(arr, N_ref):
    for i in N_ref:


def plotic(c_ref, d_ref, a_ref, b_ref, N_ref, A_ref):
    arr = createPoint_XYT(c, d, a, b, N, A)
    arrMNK = mnk(arr, N)
    plt.title("Графики функции и разброса")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.plot(arr[0], arr[1], '-b') # Исходная функция
    plt.plot(arr[0], arr[2], 'or') # Значения (points)
    plt.show()




# ----------------------------------------
# Запуск методов
# ----------------------------------------
plotic(c, d, a, b, N, A)


# ----------------------------------------