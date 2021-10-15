import matplotlib.pyplot as plt
import numpy as np
import random as rand

rand.seed(1)

# data = np.array([[-4, 2, -3, 3, 12, 6]], float)  # Вариант 9 - c, d, a, b, N, A
data = np.array([[-4, 2, -1, 2, 12, 5]], float)  # Вариант 2 - c, d, a, b, N, A
line = True  # Лин.Функция = TRUE; Парабола = FALSE
c = data[0][0]
d = data[0][1]
a = data[0][2]
b = data[0][3]
N = int(data[0][4])
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
        Yi = np.append(Yi, c_ref * Xi[-1] + d_ref) if line == True else np.append(Yi, c_ref * Xi[-1] ** 2 + d_ref)
        Ti = np.append(Ti, Yi[-1] + err)
    res = np.vstack([Xi, Yi, Ti])
    res = np.around(res, decimals=1)
    print("\nРаспределение points\n", res, "\n")
    return res

def mnk(arr, N_ref):
    if line == True:
        c_pay = (N_ref * np.dot(arr[0], arr[2]) - np.sum(arr[0]) * np.sum(arr[2])) / (
                    N_ref * np.sum(arr[0] ** 2) - np.sum(arr[0]) ** 2)
        d_pay = (np.sum(arr[2]) - c * np.sum(arr[0])) / N_ref
    else:
        c_pay = (N_ref * np.dot(arr[0] ** 2, arr[2]) - np.sum(arr[0] ** 2) * np.sum(arr[2])) / (
                    N_ref * np.sum(arr[0] ** 4) - np.sum(arr[0] ** 2) ** 2)
        d_pay = (np.sum(arr[2]) - c * np.sum(arr[0] ** 2)) / N_ref

    Zi = np.array([], float)
    for i in range(np.int64(N_ref)):
        Zi = np.append(Zi, c_pay * arr[0][i] + d_pay) if line == True else np.append(Zi, c_pay * arr[0][i] ** 2 + d_pay)
    return Zi, c_pay, d_pay

def NC(arr_x, arr_y, k):  # k - эпохи
    n = 0.05
    cc = 0
    dd = 0
    errors = []
    for _ in range(k):  # каждая эпоха
        err = 0
        for xi, yi in zip(arr_x, arr_y):
            delta = yi - (cc * xi + dd) if line == True else yi - (cc * xi**2 + dd)
            cc += n * delta * xi if line == True else n * delta * xi**2
            dd += n * delta
            err += delta ** 2
        errors.append(err)
    return cc, dd, errors, k


def plotic(c_ref, d_ref, a_ref, b_ref, N_ref, A_ref):
    arr = createPoint_XYT(c, d, a, b, N, A)
    mnk_cd = mnk(arr, N)[0]
    c_mnk = mnk(arr, N)[1]
    d_mnk = mnk(arr, N)[2]
    print("c_mnk = ", c_mnk, "\td_mnk = ", d_mnk, sep="")
    c_i, d_i, Errors, k_ep = NC(arr[0], arr[2], 20)
    print("c = ", c_i, "\td = ", d_i, sep="")
    x = np.linspace(a, b, 100)
    y = c_i * x + d_i if line == True else c_i * x**2 + d_i
    plt.plot(x, y, c = 'r', label='НС')

    # print(nc_cd[0])
    # print(nc_cd[1])
    # print(mnk_cd)
    plt.title("Графики функции и разброса.")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.plot(arr[0], arr[1], '-b', label='Исходная функция') # Исходная функция
    plt.plot(arr[0], arr[2], 'or') # Значения (points)
    plt.plot(arr[0], mnk_cd, '--og', label='Метод наименьших квадратов') # МНК
    plt.legend()
    plt.show()

    print("Ошибка итог: ", Errors[-1])

    plt.plot(range(k_ep), Errors, '--og', label='Ошибка') # МНК
    plt.show()


# ----------------------------------------
# Запуск методов
# ----------------------------------------
if __name__ == "__main__":
    plotic(c, d, a, b, N, A)

# ----------------------------------------
