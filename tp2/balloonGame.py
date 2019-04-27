'''
General animation framework taken from animation demo notes
'''
from tkinter import *
import random

####################################
# init
####################################

def init(data):
    # There is only one init, not one-per-mode
    data.mode = "homeScreen"
    data.balloon = Balloon(data.width/2, data.height*0.4, 0, 0, 5, 5, 0, [], [], 
                   data.width*0.075, data.width*0.325, data.height*0.79, data.height*0.91)
    data.clicks = data.balloon.clicks
    data.clickList = data.balloon.clickList
    data.tolerance = data.balloon.tolerances    
    data.cx = data.balloon.cx
    data.cy = data.balloon.cy
    data.hRadius = data.balloon.hRadius
    data.vRadius = data.balloon.vRadius
    data.hPlus = data.balloon.hPlus
    data.vPlus = data.balloon.vPlus
    data.runningTotal = 0
    
####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "homeScreen"):   homeScreenMousePressed(event, data)
    elif (data.mode == "playGame"):   playGameMousePressed(event, data)
    elif (data.mode == "help"):       helpMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "homeScreen"):   homeScreenKeyPressed(event, data)
    elif (data.mode == "playGame"):   playGameKeyPressed(event, data)
    elif (data.mode == "help"):       helpKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "homeScreen"):   homeScreenTimerFired(data)
    elif (data.mode == "playGame"):   playGameTimerFired(data)
    elif (data.mode == "help"):       helpTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "homeScreen"):   homeScreenRedrawAll(canvas, data)
    elif (data.mode == "playGame"):   playGameRedrawAll(canvas, data)
    elif (data.mode == "help"):       helpRedrawAll(canvas, data)

####################################
# homeScreen mode
####################################

def homeScreenMousePressed(event, data):
    if ((data.width*0.375 <= event.x <= data.width*0.625) and 
        (data.height*0.69 <= event.y <= data.height*0.81)):
        data.mode = "playGame"

def homeScreenKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.mode = "help"

def homeScreenTimerFired(data):
    pass

def homeScreenRedrawAll(canvas, data):
    introText = '''
    Maximize the amount of money you can make 
    while minimizing the amount of balloons popped!
    
    Press "h" for instructions!
    Press "p" to start pumping!
    Hit "Start" to start game!
    '''
    canvas.create_text(data.width//2, data.height//2, text=introText)
    
    # start button
    canvas.create_rectangle(data.width*0.375, data.height*0.69, 
                            data.width*0.625, data.height*0.81,
                            fill="red")
    canvas.create_text(data.width/2, data.height*0.75,text="Start",
                       fill="yellow")

####################################
# help mode
####################################

def helpMousePressed(event, data):
    pass

def helpKeyPressed(event, data):
    if (event.keysym == 'p'):
        data.mode = "playGame"
    elif (event.keysym == 'a'):
        data.mode = "homeScreen"

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    directionText = '''
    Hit "Pump" to pump balloon
    Hit "Collect" to collect earnings so far
    Press "a" to get back to home screen
    '''
    canvas.create_text(data.width//2, data.height//2, text=directionText)
    
    
####################################
# playGame mode
####################################
# ask about (similar to the sequential question), how to loop through balloons until hit 30 balloons
# also how to 'embed' a 'results' screen and/or popup between each

class Balloon(object):
    def __init__(self, cx, cy, hRadius, vRadius, hPlus, vPlus, clicks, clickList, tolerances, 
                 collectButtonX1, collectButtonX2, collectButtonY1, collectButtonY2):
        self.cx = cx
        self.cy = cy
        self.hRadius = hRadius
        self.vRadius = vRadius
        self.hPlus = hPlus
        self.vPlus = vPlus
        self.clicks = clicks
        self.clickList = clickList
        self.tolerances = tolerances
        for i in range(20):
            tolerance = random.randint(1,32)
            self.tolerances.append(tolerance)
        self.currTotal = 0
        self.collectButtonX1 = collectButtonX1
        self.collectButtonX2 = collectButtonX2
        self.collectButtonY1 = collectButtonY1
        self.collectButtonY2 = collectButtonY2
    
    def drawBalloon(self, canvas):
        canvas.create_oval(self.cx-self.hRadius,self.cy-self.vRadius,
                           self.cx+self.hRadius,self.cy+self.vRadius,
                           fill="red")
    
    def drawPoppedBalloon():
        canvas.create_text(self.cx,self.cy,"POPPED")
    
    def grow(self, x, y, popButtonX1, popButtonX2, popButtonY1, popButtonY2):
        self.popButtonX1 = popButtonX1
        self.popButtonX2 = popButtonX2
        self.popButtonY1 = popButtonY1
        self.popButtonY2 = popButtonY2
        if ((self.popButtonX1 <= x <= self.popButtonX2) and 
            (self.popButtonY1 <= y <= self.popButtonY2)):
            self.hRadius += self.hPlus
            self.vRadius += self.vPlus
            self.clicks += 1
            self.currTotal += .05
    
    def collectButton(self, x, y):
        return (self.collectButtonX1 <= x <= self.collectButtonX2) and (self.collectButtonY1 <= y <= self.collectButtonY2)
    
    def isPopped(self, popIndex):
        self.popIndex = popIndex
        return self.clicks > self.popIndex
    
    def popBalloon(self):
        self.drawPoppedBalloon()
                 
def playGameMousePressed(event, data):
    index = 0
    popIndex = data.balloon.tolerances[index]
    if not data.balloon.isPopped(popIndex):
        data.balloon.grow(event.x, event.y, data.width*0.375, data.width*0.625, data.height*0.79, data.height*0.91)
    
    else:
        data.clickList.append(data.clicks)
        data.balloon.currTotal = 0
        data.balloon = Balloon(data.width/2, data.height*0.4, 0, 0, 5, 5, 0, [], [], 
                               data.width*0.075, data.width*0.325, data.height*0.79, data.height*0.91)
        
        if index < len(data.tolerance):
            index += 1
    
    if data.balloon.collectButton(event.x, event.y):
        data.clickList.append(data.clicks)
        data.runningTotal += data.balloon.currTotal
        data.balloon.currTotal = 0
        
    if index < len(data.balloon.tolerances):
        index += 1
    

def playGameKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.mode = "help"

def playGameTimerFired(data):
    pass

def playGameRedrawAll(canvas, data):
    # collect button
    canvas.create_rectangle(data.width*0.075, data.height*0.79, 
                            data.width*0.325, data.height*0.91,
                            fill="green")
    canvas.create_text(data.width/5, data.height*0.85,text="Collect",
                       fill="white")
    # pump button
    canvas.create_rectangle(data.width*0.375, data.height*0.79, 
                            data.width*0.625, data.height*0.91,
                            fill="red")
    canvas.create_text(data.width/2, data.height*0.85,text="Pump",
                       fill="yellow")
    # draw stats
    canvas.create_rectangle(data.width*0.69,data.height*0.79,
                            data.width*0.99,data.height*0.91,
                            outline="black")
    canvas.create_text(data.width*0.7,data.height*0.85,
                       text="Current Earnings:" + str(data.balloon.currTotal),
                       anchor="nw")
    canvas.create_text(data.width*0.7,data.height*0.85,
                       text="Cumulative Earnings:" + str(data.runningTotal),
                       anchor="sw")
    # draw balloon
    data.balloon.drawBalloon(canvas)
    # where to draw popped balloon?
    # data.balloon.popBalloon()

####################################
# use the run function as-is
####################################

def runBalloonGame(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
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

runBalloonGame(800, 600)