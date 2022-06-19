from tkinter import *
from tkinter import messagebox
import numpy as np

import board as b
import game as g

#initialize board with size specified
def createGUI():   
    board = b.Board(5)
    
    root = Tk()
    root.title('Loopover')
    #root.geometry('1000x1000')
    root.iconbitmap('sources/ico/loopover.ico')

    #create squares
    buttons = [[None for _ in range(board.size)] for _ in range(board.size)]
    for y, row in enumerate(buttons):
        for x, button in enumerate(row):
            #finds color
            R = int(round(255*((board.size-x)/board.size)))
            G = int(round(255*((y)/board.size)))
            B = int(round(255*((x)/board.size)))
            hex = '#%02x%02x%02x' % (R,G,B)

            #creates button
            buttons[y][x] = Button(root, 
                text=str(board.board[y][x]+1), 
                font=('Helvetica',20), 
                height=3, width=7, 
                bg=hex, 
                command=lambda col=x, row=y : onClickBoardButton(board, col, row)
            )

            #grid buttons to screen
            buttons[y][x].grid(row=y, column=x)
    
    # Keyboard bindings
    root.bind('<Left>', lambda event: board.moveLeft)

    root.focus_set()

    root.mainloop()


def leftEvent():
    print("hi")

def onClickBoardButton(board, y, x):
    board.setCoordinates(x, y)
    print(board.y, board.x)
