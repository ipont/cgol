import os
import time
import random
import numpy as np

# Any live cell with fewer than two live neighbors dies, as if by underpopulation.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

def display(arr):
    os.system('clear')
    for i in arr:
        for x in i:
            if x == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def generate(size):
    arr = np.random.randint(2, size=(size, size))
    return arr

def update(arr):
    print("update")

arr = generate(10)
display(arr)