'''
General animation framework taken from oopyDotsDemo.py
'''

import random
from tkinter import *

class Character(object):
    # Model
    def __init__(self):
        self.figurine = PhotoImage(file="dragon.gif")

    # View
    def draw(self, canvas):
        canvas.create_image(data.width*0.8,data.height*0.9,anchor=E,image=self.figurine)

## Core animation code

def init(data):
    data.fig = Character()

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_rectangle(data.width/5,0,4*data.width/5,data.height,fill="cyan")
    data.fig.draw(canvas)
    # canvas.create_oval(data.width*0.65-10,data.height*0.85-10,data.width*0.65+10,data.height*0.85+10,fill="red")


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='black', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 400)