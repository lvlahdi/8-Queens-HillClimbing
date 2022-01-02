#!/usr/bin/env python3

# <============================== libraries ==============================> #
import random

# <============================== functions ==============================> #

# it will create a initial state of queens for us :
def randomRestart():
    columnList = [0] * 8
    for col in range(8):
        columnList[col] = random.randint(1, 8)
    return columnList

# draw queens position on the board
'''
the following function, display 8x8 chess board and writes 0 everywhere
until our given column number equals to the row number. in this case, it
will write X as a queen instead of writing 0 in that position.
'''
def printBoard(columnList):
    for row in range(8, 0, -1):
        for col in range(8):
            if columnList[col] == row:
                print("X", end="  ")
            else:
                print(0, end="  ")
        print()

def captureNum(columnList):
    captureCounter = 0
    for i in range(0, len(columnList) - 1):
        for j in range(i + 1, len(columnList)):
            if columnList[i] == columnList[j]:
                captureCounter += 1
            if (columnList[i] - columnList[j]) == i - j or (columnList[i] - columnList[j]) == -(i - j): # BUG
                captureCounter += 1
    return captureCounter

# FIXME
# [x]
def findCaptures(columnList):
    captureList = [[0 for i in range(8)] for i in range(8)]  # NOTE: list of locations where comparisons will be discarded
    # BUG
    for m in range(8):
        # to find smallest number of attacking queens number for next iteration, every location is tried therefore initial locations are kept
        copyColumnList = columnList.copy()
        for n in range(8):
            if columnList[m] == n + 1:  # if queens are where they were before
                captureList[m][n] = captureNum(columnList)
                continue
            elif copyColumnList[m] != n + 1:
                copyColumnList[m] = n + 1
                captureList[m][n] = captureNum(copyColumnList)
    return captureList

# <============================== initializing variables ==============================> #

randomRestartList = []
relocationList = []
# queensPositions = [0] * 8

# <============================== main body ==============================> #

# display queens positions on the board
queensPositions = randomRestart()
print("Queens positions on the column : ", queensPositions)
print("Queens initial position: ")
print('\n***********************\n')
printBoard(queensPositions)
print('\n***********************\n')
print("==========================================================================")

copyQueensPosition = queensPositions.copy()
# captureNumList = [[0 for i in range(8)] for i in range(8)]
relocationCounter = 0

# TODO: complete these to reduce system sources usage and prevent from doing additional nested loops :
# [ ] captureNum(queensPositions) :
# [ ] findCaptures(queensPositions) :


while captureNum(queensPositions) > 0:
    # do it until there is no capture
    relocationCounter += 1
    print("Step #{} \n".format(relocationCounter))
    print("*    %s Queens captures each other: \n" %(captureNum(queensPositions)))
    print("*    Queens positions on columns before changing: \n=>   ", queensPositions)

    captureNumList = findCaptures(queensPositions)
    smallestCap = captureNum(queensPositions)  # assigning initial capture number before finding smallest capture number

    column, row = -1, -1  # indicates the index that has smallest number of attacking queen
    for i in range(8):
        for j in range(8):
            if captureNumList[i][j] < smallestCap:
                smallestCap = captureNumList[i][j]
                column, row = i, j
    # print("column, row: ", column, ",", row)
    print("\n*    %s Queens captures each other after relocation(Smallest possible amount of captures)\n" %(smallestCap))
    if column != -1:  # if column or row values changes that means we find next position
        queensPositions[column] = row + 1
        print("\n*    Queens positions columns after relocation a queen: \n=>   ", queensPositions)
    else:
        # random restart
        print("felt in local optimum, random restarting...\n")
        queensPositions = randomRestart()
        copyQueensPosition = queensPositions.copy()
        print("*    Queens positions columns after random restart: \n=>   ", queensPositions)
        print('\n***********************\n')
        printBoard(queensPositions)
        print('\n***********************\n')
    # print("capture counter: ", captureNum(queensPositions))

    print("==========================================================================")

print("*    Final queens positions on columns : ", queensPositions)
print('\n***********************\n')
printBoard(queensPositions)
print('\n***********************\n')# print("capture counter: ", captureNum(queensPositions))
relocationList.append(relocationCounter)