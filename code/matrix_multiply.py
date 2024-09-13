#!/usr/bin/python

import numpy as np


def matrix_multiply(A, B):
    if len(A) == 0 or len(B) == 0 or len(A[0]) != len(B):
        exit("shape error")

    m = len(A)
    n = len(A[0])
    p = len(B[0])

    C = [[0 for _ in range(p)] for _ in range(m)]

    # A: m*n
    # B: n*p
    # C: m*p

    for i in range(m):
        for k in range(p):
            for j in range(n):
                C[i][k] += A[i][j] * B[j][k]

    return C


def checkResult(A, B, C):
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)
    expected_C = np.dot(A, B)
    print(np.array_equal(C, expected_C))


if __name__ == "__main__":
    A = [[1, 2, 3], [1, 2, 3]]  # 2*3
    B = [[1, 2], [1, 2], [1, 2]]  # 3*2

    C = matrix_multiply(A, B)

    checkResult(A, B, C)
