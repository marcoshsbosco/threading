import random


class Matrix:
    def __init__(self, size, zeroes=False):
        self.size = size  # all matrices are squares

        # whether matrix should initialize with random numbers or with 0s
        if not zeroes:
            self.matrix = [[random.randint(0, 4) for y in range(size)] for x in range(size)]
        else:
            self.matrix = [[0 for y in range(size)] for x in range(size)]


    def __str__(self):  # matrix representation for print() calls
        s = ""

        for i in range(self.size):
            for j in range(self.size):
                s += f"{self.matrix[i][j]:02} "

            s += "\n"

        return s
