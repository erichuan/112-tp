from tkinter import *
import random

def init(data):
    data.rows = data.cols = 8
    data.margin = 15
    data.cellSize = (data.height-2*data.margin)//data.rows
    data.board = [([None]*data.cols) for row in range(data.rows)]
    data.radius = data.cellSize * 0.4
    data.board[3][4] = data.board[4][3] = "black"
    data.board[3][3] = data.board[4][4] = "white"
    
def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            cell = drawCell(canvas, data, row, col)

def drawCell(canvas, data, row, col):
    x0 = data.margin + col * data.cellSize
    y0 = data.margin + row * data.cellSize
    x1 = x0 + data.cellSize
    y1 = y0 + data.cellSize
    canvas.create_rectangle(x0, y0, x1, y1)
    
def drawChip(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            if data.board[row][col] == None:
                cx = data.margin + data.cellSize * (col + 0.5)
                cy = data.margin + data.cellSize * (row + 0.5)
                canvas.create_oval(cx-data.radius, cy-data.radius, 
                                   cx+data.radius, cy+data.radius,
                                   fill=data.board[row][col]) 

def drawStartingChips(canvas, data):
    for row in range(3,5):
        for col in range(3,5):
            cx = data.margin + data.cellSize * (col + 0.5)
            cy = data.margin + data.cellSize * (row + 0.5)
            canvas.create_oval(cx-data.radius, cy-data.radius, 
                               cx+data.radius, cy+data.radius,
                               fill=data.board[row][col])

def drawScore(canvas, data):
    canvas.create_oval(data.width*0.75, 
                       data.margin+2*data.cellSize,
                       data.width*0.75+2*data.radius,
                       data.margin+2*data.cellSize+2*data.radius,
                       fill="black")
    canvas.create_text(data.width*0.75+2*data.radius+20,
                       data.margin+2*data.cellSize+data.radius,
                       text="x " + str(data.board.count("black")))
    canvas.create_oval(data.width*0.75, 
                       data.margin+4*data.cellSize,
                       data.width*0.75+2*data.radius,
                       data.margin+4*data.cellSize+2*data.radius,
                       fill="white")
    canvas.create_text(data.width*0.75+2*data.radius+20,
                       data.margin+4*data.cellSize+data.radius,
                       text="x " + str(data.board.count("white")))

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawBoard(canvas, data)
    canvas.create_rectangle(data.height,0,data.width,data.height,fill="lime") 
    canvas.create_line(data.height,0,data.height,data.height,fill="black",width=5)
    
    drawStartingChips(canvas, data)
    drawScore(canvas, data) 

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='beige', width=0)
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
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
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

run(600,400)