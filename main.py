import sequential
import utils
import time
import threaded

def test_battery(op, size):
    print(f"*Op: {op} | Size: {size}*")

    # size of the matrices from method call
    matrix_a = utils.Matrix(size=size)
    matrix_b = utils.Matrix(size=size)

    #-- sequential
    i0 = time.time()
    eval(f"sequential.{op}(matrix_a, matrix_b)")  # op is the operation (add, sub, mult)
    i1 = time.time()

    seq = i1 - i0  # time in seconds it took to run the sequential version of the operation
    print(f"Sequential execution time: {seq} s")

    #-- threaded
    i0 = time.time()
    eval(f"threaded.{op}(matrix_a, matrix_b, threads=2)")
    i1 = time.time()

    thr = i1 - i0  # time in seconds it took to run the threaded version of the operation
    print(f"Threaded execution time: {thr} s")

    print(f"Using threads is {((seq/thr - 1) * 100):.2f}% faster.\n")

test_battery("add", 10)
test_battery("sub", 10)
test_battery("mult", 10)
test_battery("add", 100)
test_battery("sub", 100)
test_battery("mult", 100)
test_battery("add", 400)
test_battery("sub", 400)
test_battery("mult", 400)


# test battery on a generic operation that takes 1 second per iteration
i0 = time.time()
sequential.generic_op(iterations=4)
i1 = time.time()
seq = i1 - i0
print(f"Sequential execution time: {seq} s\n")

# running the same 4 ops on 2 threads should cut the time in half
i0 = time.time()
threaded.generic_op(iterations=4)  # default number of threads is 2
i1 = time.time()
thr = i1 - i0
print(f"Threaded execution time: {thr} s")

print(f"Using threads is {((seq/thr - 1) * 100):.2f}% faster.\n")

# 4 iterations on 4 threads should be the same as running 1 iteration since they all run concurrently
i0 = time.time()
threaded.generic_op(iterations=4, threads=4)  # running with 4 threads this time
i1 = time.time()
thr = i1 - i0
print(f"Threaded execution time: {thr} s")

print(f"Using threads is {((seq/thr - 1) * 100):.2f}% faster.\n")
