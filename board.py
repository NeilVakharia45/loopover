import numpy as np
import random as rand

class BoardClass:
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size,size), dtype=int)
        for y, row in enumerate(self.board):
            for x, value in enumerate(row):
                self.board[y][x] = y*5+x

    def randomizeArray(self):
        rand_list = list(range(0,self.size*self.size))
        rand.shuffle(rand_list)
        for y, row in enumerate(self.board):
            for x, value in enumerate(row):
                self.board[y][x] = rand_list[y*5+x]

    def printArray(self):
        for i in self.board: print(i)
        print('')

    def moveUp(self, x, y):
        temp = self.board[y][x]
        for i in range(0,self.size-1):
            self.board[(y+i)%self.size][x]=self.board[(y+i+1)%self.size][x]
        self.board[(y-1)%self.size][x]=temp

    def moveDown(self, x, y):
        temp = self.board[y][x]
        for i in range(0,self.size-1):
            self.board[(y-i)%self.size][x]=self.board[(y-i-1)%self.size][x]
        self.board[(y+1)%self.size][x]=temp

    def moveLeft(self, x, y):
        temp = self.board[y][x]
        for i in range(0,self.size-1):
            self.board[y][(x+i)%self.size]=self.board[y][(x+i+1)%self.size]
        self.board[y][(x-1)%self.size]=temp

    def moveRight(self, x, y):
        temp = self.board[y][x]
        for i in range(0,self.size-1):
            self.board[y][(x-i)%self.size]=self.board[y][(x-i-1)%self.size]
        self.board[y][(x+1)%self.size]=temp

    def isSolved(self):
        #creates solved version of board and compares it to current
        correct_board = np.zeros((self.size,self.size), dtype=int)
        for y, row in enumerate(correct_board):
            for x, value in enumerate(row):
                correct_board[y][x] = y*5+x
        return np.array_equal(correct_board, self.board)