import matplotlib.pyplot as plt
import numpy as np
import random as rand

data = np.array([[-4, 2, -3, 3, 12, 6]], float)  # Вариант 9 - c, d, a, b, N, A

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
def createPoint_Yi(c_ref, d_ref, a_ref, b_ref, N_ref, A_ref):
    Xi = np.array([], float)
    Yi = np.array([], float)
    for i in frange(a_ref, b_ref, (b_ref - a_ref) / N_ref):
        err = A_ref * (rand.random() - 0.5)
        Xi = np.append(Xi, i)
        Yi = np.append(Yi, c_ref * Xi[-1] + d_ref)
    res = np.vstack([Xi, Yi])
    return res

print(createPoint_Yi(c, d, a, b, N))

# def transInt_Float(mass_int, N):
#     mass_float = []
#     for i in range(N):
#         mass_float.append(float(mass_int[i]))
#     return mass_float


# Xii = createPoint_Xi(data[0][2], data[0][3], data[0][4])
# Yii = createPoint_Yi(data[0][0], data[0][1], data[0][4])
# Xres = transInt_Float(Xii, data[0][4])
# Yres = transInt_Float(Yii, data[0][4])
# print(Xres)
# print(Yres)

# plt.plot(Xii, Yii, '-ro')

# one = []
# for i in range(10):
#     one.append(rand.random() - 0.5)
# print(one)
