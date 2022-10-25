import utils
import time


def add(a, b):
    res = utils.Matrix(a.size, zeroes=True)

    for i in range(a.size):
        for j in range(a.size):
            res.matrix[i][j] = a.matrix[i][j] + b.matrix[i][j]

    return res


def sub(a, b):
    res = utils.Matrix(a.size, zeroes=True)

    for i in range(a.size):
        for j in range(a.size):
            res.matrix[i][j] = a.matrix[i][j] - b.matrix[i][j]

    return res


def mult(a, b):
    res = utils.Matrix(a.size, zeroes=True)

    for i in range(a.size):
        for j in range(a.size):
            for k in range(a.size):
                res.matrix[i][j] += a.matrix[i][k] * b.matrix[k][j]

    return res


def generic_op(iterations):
    for i in range(iterations):
        print(f"i{i}: Executing code that takes 1 second to process...")
        time.sleep(1)  # literally waits for 1 second
        print(f"i{i}: Done!")
