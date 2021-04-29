#DSC 430: Python Programming - Assignment 0902: Game of Life
#Student Name: Serena Yang
#Date: Nov, 17, 2020
#Video Link: https://youtu.be/xVyA4v0FqmE
#I have not given or received any unauthorized assistance on this assignment.

import numpy as np
import math

#generates a board, which is a square two dimensional NumPy array of size s by s.
def conway(s,p):
    #set the board with p precentage of 1/0 and reshape them as matrix s*s
    board = np.random.choice([1,0], s*s, p).reshape(s,s)
    return board

#accepts a Conway board and advances it t time steps
def advance(b,t):
    #copy board as an new matrix
    next = b.copy()
    #get the length of each side of the board
    s = int(math.sqrt(b.size))
    #run t times
    for i in range(t):
        #run each side of the board one by one to get each number
        for m in range(s):
            for n in range(s):
                #check the neighber sum
                neighbers = int(b[(m-1)%s,(n-1)%s] + b[(m-1)%s,(n)] + b[(m-1)%s,(n+1)%s] +
                                 b[(m),(n-1)%s]  + b[(m),(n+1)%s] + 
                                 b[(m+1)%s,(n-1)%s] + b[(m+1)%s,(n)] + b[(m+1)%s,(n+1)%s])
                #if the cell is alive
                if b[m,n] == 1:
                    #neighber live cell is fewer than 2 or more than 3
                    if (neighbers < 2) or (neighbers > 3):
                        #the live dead
                        next[m,n] = 0
                    #neighber live cell equals to 2 or 3
                    elif (neighbers == 2) or (neighbers == 3):
                        #the cell keep alive
                        next[m,n] = 1
                #if the cell is dead
                elif b[m,n] == 0:
                    #neighber live cell equals to 3
                    if (neighbers == 3):
                        #the cell become alive
                        next[m,n] = 1

        #copy the board to the next one
        b[:] = next[:]
        #print results
        print("time " + str(i+1))
        print(next)


def main():
    #set board size, precent of cells, total running times of function advance()
    s = 10
    p = [0.1, 0.9]
    t = 5
    #call function
    b = conway(s,p)
    advance(b,t)

main()



