# import tkinter and all its functions
from ctypes import alignment
from tkinter import * 
import board as b
#import pyglet

 
root = Tk() # create root window
root.title('Loopover')
root.maxsize(900, 600)
root.minsize(900, 600)
root.geometry('900x600')
root.iconbitmap('resources/ico/loopover.ico')
root.config() # specify background color
 
# Create Frame widget
left_frame = Frame(root, width=470, height=470)
left_frame.grid(row=0, column=0, padx=20, pady=20)
 
# Create title bar within left_frame
title_bar = Frame(left_frame, width=470, height=50)
title_bar.grid(row=2, column=0, padx=0, pady=0)
# Display image in title_bar
title_image = PhotoImage(file='resources/img/title_bar.png')
Label(title_bar, image=title_image).grid(row=0,column=0, padx=0, pady=0)

# Create game board within left_frame
game_board = Frame(left_frame, width=470, height=470, bg='red')
game_board.grid(row=3, column=0, padx=0, pady=20)



root.mainloop()