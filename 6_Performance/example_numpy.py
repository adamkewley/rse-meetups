import numpy as np
import time

def inefficient_numpy_operations(n):
    matrix1 = np.eye(n)

    matrix2 = np.random.rand(n, n)
    result2 = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            result2[i, j] = matrix1[i, j] * matrix2[i, j]

    result3 = np.sum(result2)

if __name__ == "__main__":
    inefficient_numpy_operations(1000)
