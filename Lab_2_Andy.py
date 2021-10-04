import matplotlib.pyplot as plt
import numpy as np

data = np.array([-4, 2, -3, 3, 12, 6])  # Вариант 9 - c, d, a, b, N, A

arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
name_col = ["X", "Y", "Z"]
name_tab = "Таблица XYZ"


def print_matrix(arr, columns, name_table):
    print("\n", name_table, sep="")
    arr.insert(0, columns)
    arr.insert(1, ["----"]*3)
    for i in arr:
        print(*[f"{x:>5}" for x in i])
    print()

print_matrix(arr_2d, name_col, name_tab)
print_matrix(arr_2d, name_col, name_tab)