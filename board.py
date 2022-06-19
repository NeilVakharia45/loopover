import numpy as np
import random as rand

class BoardClass:

    # Defines 2D numpy array for the board
    def __init__(self, size):
        self.x=0
        self.y=0
        self.size = size
        self.board = createBoard(size)
            
    # Randomizes board
    def randomizeBoard(self):
        rand_list = list(range(0,self.size*self.size))
        rand.shuffle(rand_list)
        for y, row in enumerate(self.board):
            for x, value in enumerate(row):
                self.board[y][x] = rand_list[y*5+x]

    # Prints board to terminal
    def printArray(self):
        for i in self.board: print(i)
        print('')

    # Moves column up from x and y
    def moveUp(self, x, y):
        temp = self.board[y][x]
        for i in range(0,self.size-1):
            self.board[(y+i)%self.size][x]=self.board[(y+i+1)%self.size][x]
        self.board[(y-1)%self.size][x]=temp

    # Moves column down from x and y
    def moveDown(self, x, y):
        temp = self.board[y][x]
        for i in range(0,self.size-1):
            self.board[(y-i)%self.size][x]=self.board[(y-i-1)%self.size][x]
        self.board[(y+1)%self.size][x]=temp

    # Moves row left from x and y
    def moveLeft(self, x, y):
        temp = self.board[y][x]
        for i in range(0,self.size-1):
            self.board[y][(x+i)%self.size]=self.board[y][(x+i+1)%self.size]
        self.board[y][(x-1)%self.size]=temp

    # Move row right from x and y
    def moveRight(self, x, y):
        temp = self.board[y][x]
        for i in range(0,self.size-1):
            self.board[y][(x-i)%self.size]=self.board[y][(x-i-1)%self.size]
        self.board[y][(x+1)%self.size]=temp

    # Compares board against solved board
    def isSolved(self):
        solvedBoard=createBoard(self.size)

        return np.array_equal(solvedBoard, self.board)

def createBoard(size):
    board = np.zeros((size,size), dtype=int)
    for y, row in enumerate(board):
        for x, value in enumerate(row):
            board[y][x] = y*size+x
    return board