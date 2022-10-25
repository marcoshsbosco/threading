import utils
import threading
import time


"""
Functions preceded by 'thr_' are the actual operations being executed. Besides the actual matrix operations logic, there is also logic to delimit what any current thread should process.
Corresponding functions without 'thr_' serve to create a result matrix and to spawn the threads that are going to do the processing.
"""

def thr_add(a, b, res, parts, part):
    # delimits what is processed according to how many and which threads are running the method
    range_start = a.size // parts * part
    range_end = range_start + a.size // parts

    # this is the actual matrix addition logic
    for i in range(range_start, range_end):
        for j in range(a.size):
            res.matrix[i][j] = a.matrix[i][j] + b.matrix[i][j]


def thr_sub(a, b, res, parts, part):
    range_start = a.size // parts * part
    range_end = range_start + a.size // parts

    for i in range(range_start, range_end):
        for j in range(a.size):
            res.matrix[i][j] = a.matrix[i][j] - b.matrix[i][j]


def thr_mult(a, b, res, parts, part):
    range_start = a.size // parts * part
    range_end = range_start + a.size // parts

    for i in range(range_start, range_end):
        for j in range(a.size):
            for k in range(a.size):
                res.matrix[i][j] += a.matrix[i][k] * b.matrix[k][j]


def add(a, b, threads=2):
    res = utils.Matrix(a.size, zeroes=True)  # result matrix initialized with 0s
    thr_list = []

    # spawn threads and add them to pool
    for i in range(threads):
        thr = threading.Thread(target=thr_add, args=(a, b, res, threads, i))
        thr_list.append(thr)

    # start the execution of the threads
    for thr in thr_list:
        thr.start()

    # wait for all threads to finish before returning result
    for thr in thr_list:
        thr.join()

    return res


def sub(a, b, threads=2):
    res = utils.Matrix(a.size, zeroes=True)
    thr_list = []

    for i in range(threads):
        thr = threading.Thread(target=thr_sub, args=(a, b, res, threads, i))
        thr_list.append(thr)

    for thr in thr_list:
        thr.start()

    for thr in thr_list:
        thr.join()

    return res


def mult(a, b, threads=2):
    res = utils.Matrix(a.size, zeroes=True)
    thr_list = []

    for i in range(threads):
        thr = threading.Thread(target=thr_mult, args=(a, b, res, threads, i))
        thr_list.append(thr)

    for thr in thr_list:
        thr.start()

    for thr in thr_list:
        thr.join()

    return res


def thr_generic_op(iterations, parts, part):
    range_start = iterations // parts * part
    range_end = range_start + iterations // parts

    for i in range(range_start, range_end):
        print(f"i{i}: Executing code that takes 1 second to process...")
        time.sleep(1)
        print(f"i{i}: Done!")


def generic_op(iterations, threads=2):
    thr_list = []

    for i in range(threads):
        thr = threading.Thread(target=thr_generic_op, args=(iterations, threads, i))
        thr_list.append(thr)

    for thr in thr_list:
        thr.start()

    for thr in thr_list:
        thr.join()
