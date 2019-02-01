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

def neighbors(arr, x, y):
    neighbors = 0

    #check above
    if x + 1 < len(arr):
        i = arr[x+1]
        if i[y] == 1:
            neighbors += 1

    #check above right
    if x + 1 < len(arr):
        i = arr[x + 1]
        if y < len(i):
            if i[y] == 1:
                neighbors += 1

    # check below
    if x - 1 < 0:
        i = arr[x - 1]
        if i[y] == 1:
            neighbors += 1

    # check to right
    i = arr[x]
    if y + 1 < len(i):
        if i[y+1] == 1:
            neighbors += 1

    # check to left
    i = arr[x]
    if y - 1 < 0:
        if i[y - 1] == 1:
            neighbors += 1

    return neighbors

def update(arr):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            n = neighbors(arr, x, y)
            if arr[x][y] == 1 and n < 2:
                arr[x][y] = 0
            if arr[x][y] == 1 and n > 2:
                arr[x][y] = 0
            if arr[x][y] == 0 and n == 3:
                arr[x][y] = 1


arr = generate(20)

while True:
    display(arr)
    update(arr)
    time.sleep(1)