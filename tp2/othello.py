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
    data.numBlack = 0
    data.numWhite = 0
    NORTH = (0, -1)
    SOUTH = (0, +1)
    EAST = (+1, 0)
    WEST = (-1, 0)
    NORTHEAST = (+1, -1)
    SOUTHEAST = (+1, +1)
    SOUTHWEST = (-1, +1)
    NORTHWEST = (-1, -1)
    data.directions = [NORTH, SOUTH, EAST, WEST]
    data.diagonals = [NORTHEAST, SOUTHEAST, SOUTHWEST, NORTHWEST]
    data.otherLst = []
    data.player = "black"
    data.legalMoves = []
    
def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            cell = drawCell(canvas, data, row, col)
            if data.board[row][col] == None:
                continue
            else:
                chip = drawChip(canvas, data, row, col)

def drawCell(canvas, data, row, col):
    x0 = data.margin + col * data.cellSize
    y0 = data.margin + row * data.cellSize
    x1 = x0 + data.cellSize
    y1 = y0 + data.cellSize
    canvas.create_rectangle(x0, y0, x1, y1)
    
def drawChip(canvas, data, row, col):
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

def countBlackChips(data):
    data.numBlack = 0
    for row in range(data.rows):
        for col in range(data.cols):
            if data.board[row][col] == "black":
                data.numBlack += 1
    return data.numBlack

def countWhiteChips(data):
    data.numWhite = 0
    for row in range(data.rows):
        for col in range(data.cols):
            if data.board[row][col] == "white":
                data.numWhite += 1
    return data.numWhite

def drawScore(canvas, data):
    canvas.create_oval(data.width*0.75, 
                       data.margin+2*data.cellSize,
                       data.width*0.75+2*data.radius,
                       data.margin+2*data.cellSize+2*data.radius,
                       fill="black")
    countBlackChips(data)
    canvas.create_text(data.width*0.75+2*data.radius+20,
                       data.margin+2*data.cellSize+data.radius,
                       text="x " + str(data.numBlack))
    canvas.create_oval(data.width*0.75, 
                       data.margin+4*data.cellSize,
                       data.width*0.75+2*data.radius,
                       data.margin+4*data.cellSize+2*data.radius,
                       fill="white")
    countWhiteChips(data)
    canvas.create_text(data.width*0.75+2*data.radius+20,
                       data.margin+4*data.cellSize+data.radius,
                       text="x " + str(data.numWhite))

def isLegalMove(data, row, col):
    if data.player == "black": other = "white"
    elif data.player == "white": other = "black"
    
    for direction in data.directions:
        # check if it's not out of bounds
        if not ((0 <= row < data.rows) or (0 <= col < data.cols)):
            return False
        # check if it's not occupied space
        elif data.board[row][col] != None:
            return False 
        # check if the immediate up/down/left/right/NE/SE/SW/NW not out of bounds
        elif ((0 > row+direction[0]) or (row+direction[0] >= data.rows) or (0 > col+direction[1]) or (col+direction[1] >= data.cols)):
            return False
        # check if there's no same color piece to the immediate up/down/left/right/NE/SE/SW/NW
        elif data.board[row+direction[0]][col+direction[1]] == data.player:
            return False
        # check if it's different color piece and if so, proceed to check if legal move
        elif (data.board[row+direction[0]][col+direction[1]] == other):
            return True 
            
def getCell(x,y, data):
    row = (x-data.margin)//data.cellSize
    col = (y-data.margin)//data.cellSize
    return (row, col)

def flip(data):
    for other in data.otherLst:
        data.board[other[0]][other[1]] = data.player

def ripple(data, row, col):
    if data.player == "black": other = "white"
    elif data.player == "white": other = "black"
    
    for direction in data.directions:
        if data.board[row+direction[0]][col+direction[1]] == other:
            data.otherLst.append((row+direction[0], col+direction[1]))
            increment = 2
            while data.board[row+direction[0]*increment][col+direction[1]*increment] == other:
                data.otherLst.append((row+direction[0]*increment, col+direction[1]*increment))
                increment += 1
            if data.board[row+direction[0]*increment][col+direction[1]*increment] == data.player:
                flip(data)
            data.otherLst = []
    
    for diagonal in data.diagonals:
        if data.board[row+diagonal[0]][col+diagonal[1]] == other:
            data.otherLst.append((row+diagonal[0], col+diagonal[1]))
            increment = 2
            while data.board[row+diagonal[0]*increment][col+diagonal[1]*increment] == other:
                data.otherLst.append((row+diagonal[0]*increment, col+diagonal[1]*increment))
                increment += 1
            if data.board[row+diagonal[0]*increment][col+diagonal[1]*increment] == data.player:
                flip(data)
            data.otherLst = []
    
def makeMove(data, a, b):
    (currRow, currCol) = getCell(a, b, data)
    move = (currRow, currCol)
    
    if move in data.legalMoves:
        data.board[currRow][currCol] = data.player
        ripple(data, currRow, currCol)
        
        if data.player == "black": data.player = "white"
        elif data.player == "white": data.player = "black"
        
    data.legalMoves = []

## things to do to get towards implementing game AI
def getLegalMoves(data):
    for row in range(data.rows):
        for col in range(data.cols):
            if isLegalMove(data, row, col):
                data.legalMoves.append((row, col))

def gameOver(data):
    # if entire board filled
    fillCount = 0
    for row in data.rows:
        for col in data.cols:
            if data.board[row][col] != None:
                fillCount += 1
    if fillCount == 64:
        return True
    
    # if both players can't make moves (no legal moves)
    if ((data.legalMoves == [] and data.player == "black") and 
        (data.legalMoves == [] and data.player == "white")):
        return True






##

def mousePressed(event, data):
    getLegalMoves(data)
    makeMove(data, event.y, event.x)
        
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