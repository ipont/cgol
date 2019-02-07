# CSC 310: Conway's Game of Life
# Isaac Pontarelli
# Sean Polin
# Alec Smith

import os
import time
import numpy as np


# get size of board
def get_size():
    valid_type = False
    while valid_type == False:
        try:
            size = int(input("Enter board size: "))
            valid_type = True
        except ValueError:
            print("Invalid input, try again")
    return size


# get number of generations
def get_gen():
    valid_type = False
    while valid_type == False:
        try:
            gen = int(input("Enter the number of generations (-1 for infinite): "))
            valid_type = True
        except ValueError:
            print("Invalid input, try again")
    return gen


# display board nicely
def display(arr):
    # clear screen
    if (os.name == "nt"):
        os.system('cls')
    else:
        os.system('clear')
    print()
    print()
    # print 1 as '*' an 0 as ' '
    for i in arr:
        for x in i:
            if x == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def generate(size):
    # Generates a pseudo random nxn 2d array of 1s and 0s
    arr = np.random.randint(2, size=(size, size))
    return arr


def neighbors(arr, x, y):
    neighbors = 0

    #check below
    if x + 1 < len(arr):
        i = arr[x+1]
        if i[y] == 1:
            neighbors += 1

    #check below right
    if x + 1 < len(arr):
        i = arr[x + 1]
        if y + 1 < len(i):
            if i[y + 1] == 1:
                neighbors += 1

    #check below left
    if x + 1 < len(arr):
        i = arr[x + 1]
        if y - 1 >= 0:
            if i[y - 1] == 1:
                neighbors += 1

    # check above
    if x - 1 >= 0:
        i = arr[x - 1]
        if i[y] == 1:
            neighbors += 1

    #check above right
    if x - 1 >= 0:
        i = arr[x - 1]
        if y + 1 < len(i):
            if i[y + 1] == 1:
                neighbors += 1

    #check above left
    if x - 1 >= 0:
        i = arr[x - 1]
        if y - 1 >= 0:
            if i[y - 1] == 1:
                neighbors += 1

    # check to right
    i = arr[x]
    if y + 1 < len(i):
        if i[y+1] == 1:
            neighbors += 1

    # check to left
    i = arr[x]
    if y - 1 >= 0:
        if i[y - 1] == 1:
            neighbors += 1

    return neighbors


# make decisions on whether a cell should live or die
def update(arr):
    # updated array
    narr = arr
    for x in range(len(arr)):
        for y in range(len(arr)):
            n = neighbors(arr, x, y)
            if arr[x][y] == 1 and n < 2:
                narr[x][y] = 0
            if arr[x][y] == 1 and n == 2:
                narr[x][y] = 1
            if arr[x][y] == 1 and n == 3:
                narr[x][y] = 1
            if arr[x][y] == 1 and n > 3:
                narr[x][y] = 0
            if arr[x][y] == 0 and n == 3:
                narr[x][y] = 1
    return narr


# top level function
def main():
    # get user input
    size = get_size()
    gens = get_gen()
    # new random board
    arr = generate(size)

    # infinite generations
    if gens == -1:
        while True:
            display(arr)
            arr = update(arr)
            time.sleep(1)

    # finite generations
    for i in range(gens):
        display(arr)
        arr = update(arr)
        time.sleep(1)

main()