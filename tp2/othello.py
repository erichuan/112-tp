'''
General animation framework taken from 112 course notes
'''
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
    NORTH = (-1, 0)
    SOUTH = (+1, 0)
    EAST = (0, +1)
    WEST = (0, -1)
    NORTHEAST = (-1, +1)
    SOUTHEAST = (+1, +1)
    SOUTHWEST = (+1, -1)
    NORTHWEST = (-1, -1)
    data.directions = [NORTH, SOUTH, EAST, WEST, NORTHEAST, SOUTHEAST, SOUTHWEST, NORTHWEST]
    data.otherLst = []
    data.player = "black"
    data.legalMoves = []
    data.whiteChips = []
    data.tmpMoves = []
    data.help = False
    data.gameOver = False
    
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


def getLegalHumanMoves(data, row, col):
    if data.board[row][col] == None:
        for direction in data.directions:
            tmpRow = row+direction[0]
            tmpCol = col+direction[1]
            if ((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)):
                if data.board[tmpRow][tmpCol] == "white":
                    while (((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)) and 
                            (data.board[tmpRow][tmpCol] == "white")):
                        tmpRow += direction[0]
                        tmpCol += direction[1]
                    if (((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)) and 
                        (data.board[tmpRow][tmpCol] == "black")):
                        data.legalMoves.append((row, col))


def getLegalAIMoves(data, chips):
    for chip in chips:
        for direction in data.directions:
            tmpRow = chip[0]+direction[0]
            tmpCol = chip[1]+direction[1]
            if ((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)):
                if data.board[tmpRow][tmpCol] == "black":
                    while (((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)) and 
                           (data.board[tmpRow][tmpCol] == "black")):
                        tmpRow += direction[0]
                        tmpCol += direction[1]
                    if (((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)) and 
                        (data.board[tmpRow][tmpCol] == None)):
                        data.legalMoves.append((tmpRow, tmpCol))


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
        tmpRow = row+direction[0]
        tmpCol = col+direction[1]
        if ((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)):
            while (((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)) and 
                    (data.board[tmpRow][tmpCol] == other)):
                data.otherLst.append((tmpRow, tmpCol))
                tmpRow += direction[0]
                tmpCol += direction[1]
            if (((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)) and 
                (data.board[tmpRow][tmpCol] == data.player)):
                flip(data)
            data.otherLst = []
    
def getHumanMove(a, b, data):
    (currRow, currCol) = getCell(a, b, data)
    return (currRow, currCol)    
    
def getAIMove(data):
    move = minimize(data) # AI to minimize black chips
    return move

## implementing (simple) minimax!
# AI ("white") to minimize human ("black") chips
# in other words, AI will be 'MinnieMove' and human is 'MaxieMove'

def tempRipple(data, row, col, player):
    if player == "black": other = "white"
    elif player == "white": other = "black"
    
    for direction in data.directions:
        tmpRow = row+direction[0]
        tmpCol = col+direction[1]
        if ((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)):
            while (((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)) and 
                   (data.board[tmpRow][tmpCol] == other)):
                data.otherLst.append((tmpRow, tmpCol))
                tmpRow += direction[0]
                tmpCol += direction[1]
            if (((0 <= tmpRow < data.rows) and (0 <= tmpCol < data.cols)) and 
                (data.board[tmpRow][tmpCol] == player)):
                for other in data.otherLst:
                    data.board[other[0]][other[1]] = player
                    data.tmpMoves.append((other[0], other[1]))
            data.otherLst = []

def tempMove(data, move, player):
    data.board[move[0]][move[1]] = player
    data.tmpMoves.append((move[0], move[1]))
    tempRipple(data, move[0], move[1], player)

def unmakeTempMove(data, player):
    if player == "black": other = "white"
    elif player == "white": other = "black"
    
    firstMove = data.tmpMoves.pop(0)
    data.board[firstMove[0]][firstMove[1]] = None
    
    for move in data.tmpMoves:
        data.board[move[0]][move[1]] = other
    
    data.tmpMoves = []
        
def minimize(data):
    if not gameOver(data):
        bestMove = None
        bestScore = float("inf")
        tmpPlayer = "white"
        for legalMove in data.legalMoves:
            tmpMove = tempMove(data, legalMove, tmpPlayer)
            countBlackChips(data)
            if data.numBlack <= bestScore:
                bestMove = legalMove
                bestScore = data.numBlack
            unmakeTempMove(data, tmpPlayer)
            countBlackChips(data)
        return bestMove

def getAIChips(data):
    whiteChips = []
    for row in range(data.rows):
        for col in range(data.cols):
            if data.board[row][col] == "white":
                whiteChips.append((row, col))
    return whiteChips

def makeMove(data, move):
    if move in data.legalMoves:
        data.board[move[0]][move[1]] = data.player
        ripple(data, move[0], move[1])
        
        if data.player == "black": data.player = "white"
        elif data.player == "white": data.player = "black"
        
        data.legalMoves = []

def completeBoard(data):
    fillCount = 0
    for row in range(data.rows):
        for col in range(data.cols):
            if data.board[row][col] == None:
                return False
    return True

def gameOver(data):
    # if entire board filled or both players can't make moves (no legal moves)
    if (completeBoard(data) or ((data.legalMoves == [] and data.player == "black") and (data.legalMoves == [] and data.player == "white"))):
        data.gameOver = not data.gameOver

def drawEndGameMessage(canvas, data):
    canvas.create_rectangle(data.width/2-50,data.height/2-20,data.width/2+50,data.height/2+20,fill="red")
    
    if data.numBlack > data.numWhite:
        canvas.create_text(data.width/2, data.height/2, text="Black won!",fill="yellow")
    elif data.numWhite > data.numBlack:
        canvas.create_text(data.width/2, data.height/2, text="White won!",fill="yellow")
    else:
        canvas.create_text(data.width/2, data.height/2, text="It's a tie!'",fill="yellow")

def drawHelp(canvas, data):
    canvas.create_rectangle(data.width/2-250,data.height/2-50,data.width/2+250,data.height/2+50,fill="red")
    
    helpText = '''
    There might be more here (i.e. AI to give human move suggestions) 
    
    Press 'space' to close this window
    '''
    canvas.create_text(data.width/2, data.height/2, text=helpText,fill="white")

def mousePressed(event, data):
    gameOver(data)
    
    if not data.gameOver:
        if data.player == "black":
            move = getHumanMove(event.y, event.x, data)
            getLegalHumanMoves(data, move[0], move[1])
            makeMove(data, move)
            
        if data.player == "white":
            chips = getAIChips(data)
            getLegalAIMoves(data, chips)
            move = getAIMove(data)
            makeMove(data, move)
            
            data.moves = []
        
def keyPressed(event, data):
    if event.keysym == "h":
        data.help = True
    elif event.keysym == "space":
        data.help = False
    elif event.keysym == "e":
        data.gameOver = not data.gameOver
    elif event.keysym == "r":
        init(data)

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawBoard(canvas, data)
    canvas.create_rectangle(data.height,0,data.width,data.height,fill="lime") 
    canvas.create_line(data.height,0,data.height,data.height,fill="black",width=5)
    
    help1 = '''
    Press 'h' for help
    Press 'e' to exit
    Press 'r' to play again
    '''
    canvas.create_text(data.width*0.75+2*data.radius+20,
                       data.margin+7*data.cellSize+data.radius,text=help1,fill="black")
    
    drawStartingChips(canvas, data)
    drawScore(canvas, data) 
    
    if data.help:
        drawHelp(canvas, data)
    else:
        drawBoard(canvas, data)
    
    if data.gameOver:
        drawEndGameMessage(canvas, data)
 

####################################
# use the run function as-is
####################################

def runOthello(width=300, height=300):
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

runOthello(600,400)