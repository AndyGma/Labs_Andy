import numpy as np

def createPoint_Yi():
    Xi = np.array([-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5], float)
    Yi = np.array([], float)
    for i in range(12):
        res = np.append(Yi, [-4 * Xi + 2])
    return res

print(createPoint_Yi())