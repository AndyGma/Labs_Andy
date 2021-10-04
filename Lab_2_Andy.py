import matplotlib.pyplot as plt
import numpy as np
import random as rand

data = np.array([[-4, 2, -3, 3, 12, 6]], float)  # Вариант 9 - c, d, a, b, N, A


def print_matrix(arr, columns, name_table):
    print("\n", name_table, sep="")
    arr.insert(0, columns)
    arr.insert(1, ["----"]*len(columns))
    for i in arr:
        print(*[f"{x:>5}" for x in i])
    print()
    arr.pop(1)
    arr.pop(0)
def frange(a, b, jump):
    while a < b:
        yield a
        a += jump
def createPoint_Xi(a, b, N):
    ret = []
    for i in frange(a, b, (b - a) / N):
        ret.append(i)
    return ret
def createPoint_Yi(c, d, N):
    Xi = createPoint_Xi(data[0][2], data[0][3], data[0][4])
    Yi = []
    for i in range(N):
        Yi.append(c * Xi[i] + d)
    return Yi
def transInt_Float(mass_int, N):
    mass_float = []
    for i in range(N):
        mass_float.append(float(mass_int[i]))
    return mass_float


print_matrix(data, ["c", "d", "a", "b", "N", "A"], "Исходные данные")
Xii = createPoint_Xi(data[0][2], data[0][3], data[0][4])
Yii = createPoint_Yi(data[0][0], data[0][1], data[0][4])
Xres = transInt_Float(Xii, data[0][4])
Yres = transInt_Float(Yii, data[0][4])
print(Xres)
print(Yres)

# plt.plot(Xii, Yii, '-ro')

# one = []
# for i in range(10):
#     one.append(rand.random() - 0.5)
# print(one)
