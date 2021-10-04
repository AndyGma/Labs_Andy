import matplotlib.pyplot as plt
import numpy as np

data = [[-4, 2, -3, 3, 12, 6]]  # Вариант 9 - c, d, a, b, N, A


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


print_matrix(data, ["c", "d", "a", "b", "N", "A"], "Исходные данные")
print(createPoint_Xi(data[0][2], data[0][3], data[0][4]))
