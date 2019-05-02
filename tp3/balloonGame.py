'''
General animation framework taken from animation demo notes
'''
from tkinter import *
import random

def balloonInit(data):
    data.balloon = Balloon(data.width/2, data.height*0.4, 0, 0, 5, 5, 0, [], [], 
                   data.width*0.075, data.width*0.325, data.height*0.79, data.height*0.91, False)
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
    data.isCollected = data.balloon.isCollected
    data.oppCost = 0
    data.accuracy = []
    data.index = 0
    
# ask how to 'embed' a 'results' screen and/or popup between each

class Balloon(object):
    def __init__(self, cx, cy, hRadius, vRadius, hPlus, vPlus, clicks, clickList, tolerances, 
                 collectButtonX1, collectButtonX2, collectButtonY1, collectButtonY2, isCollected):
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
        self.isCollected = isCollected
    
    def drawBalloon(self, canvas):
        canvas.create_oval(self.cx-self.hRadius,self.cy-self.vRadius,
                           self.cx+self.hRadius,self.cy+self.vRadius,
                           fill="red")
    
    def drawPoppedBalloon(self, canvas):
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
            self.currTotal += .10
    
    def collectButton(self, x, y):
        self.isCollected = True
        return (self.collectButtonX1 <= x <= self.collectButtonX2) and (self.collectButtonY1 <= y <= self.collectButtonY2)
    
    def isPopped(self, popIndex):
        self.popIndex = popIndex
        return self.clicks > self.popIndex

def gameOver(data):
    return data.index >= len(data.tolerance)

def balloonMousePressed(event, data):
    if not gameOver(data):
        popIndex = data.balloon.tolerances[data.index]
        if not data.balloon.isPopped(popIndex):
            data.balloon.grow(event.x, event.y, data.width*0.375, data.width*0.625, data.height*0.79, data.height*0.91)
        
        else:
            data.clickList.append(data.clicks)
            data.accuracy.append(0)
            data.balloon.currTotal = 0
            data.balloon = Balloon(data.width/2, data.height*0.4, 0, 0, 5, 5, 0, [], [], 
                                data.width*0.075, data.width*0.325, data.height*0.79, data.height*0.91, False)
            
            data.index += 1
        
        if data.balloon.collectButton(event.x, event.y):
            data.clickList.append(data.clicks)
            data.oppCost = popIndex - data.clicks
            data.accuracy.append(1)
            data.runningTotal += data.balloon.currTotal
            data.balloon.currTotal = 0
            data.oppCost = 0
            data.balloon = Balloon(data.width/2, data.height*0.4, 0, 0, 5, 5, 0, [], [], 
                                data.width*0.075, data.width*0.325, data.height*0.79, data.height*0.91, False)
            
            data.index += 1    

def balloonKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.mode = "help"
    elif (event.keysym == 'm'):
        data.mode = "mainLoop"
    elif (event.keysym == 'x'):
        data.index = len(data.tolerance)

def balloonTimerFired(data):
    pass

def balloonRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="lime")
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
                       fill="white")
    # draw stats
    canvas.create_rectangle(data.width*0.69,data.height*0.79,
                            data.width*0.99,data.height*0.91,
                            fill="yellow",outline="black")
    canvas.create_text(data.width*0.7,data.height*0.85,
                       text="Current Earnings: %0.2f" % (data.balloon.currTotal),
                       anchor="nw")
    canvas.create_text(data.width*0.7,data.height*0.85,
                       text="Cumulative Earnings: %0.2f" % (data.runningTotal),
                       anchor="sw")
    canvas.create_text(data.width*0.8, data.height*0.95, text="Press 'm' for mainLoop")
    canvas.create_text(data.width*0.8, data.height*0.98, text="Press 'x' to end game")
    # draw balloon
    data.balloon.drawBalloon(canvas)
    
    # draw opportunity cost stats    
    if data.isCollected:
        canvas.create_rectangle(data.width/2-200,data.height/2-50,data.width/2+200,data.height/2+50,fill="cyan")
        canvas.create_text(data.width/2, data.height/2-10, text="Balloon would've popped at " + str(data.tolerance[data.index]) + "pumps",fill="black")
        canvas.create_text(data.width/2, data.height/2, text="Your pumps: %0.2f" % (data.clicks), fill="black")
        canvas.create_text(data.width/2, data.height/2+10, text="Opportunity cost: %0.2f" % (data.oppCost), fill="black")
    else:
        data.balloon.drawBalloon(canvas)
    
    if gameOver(data):
        canvas.create_rectangle(data.width/2-250,data.height/2-100,data.width/2+250,data.height/2+100,fill="red")
        canvas.create_text(data.width/2, data.height/2-20,text="Your total earnings: $%0.2f" % (data.runningTotal), fill="white")
        canvas.create_text(data.width/2, data.height/2,text="You popped %d out of %d balloons" % (data.accuracy.count(0), len(data.accuracy)), fill="white")
        canvas.create_text(data.width/2, data.height/2+40, text="Press 'm' to return to main loop!",fill="white")

####################################
# use the run function as-is
####################################

# def runBalloonGame(width=300, height=300):
#     def redrawAllWrapper(canvas, data):
#         canvas.delete(ALL)
#         canvas.create_rectangle(0, 0, data.width, data.height,
#                                 fill='white', width=0)
#         balloonRedrawAll(canvas, data)
#         canvas.update()    
# 
#     def mousePressedWrapper(event, canvas, data):
#         balloonMousePressed(event, data)
#         redrawAllWrapper(canvas, data)
# 
#     def keyPressedWrapper(event, canvas, data):
#         balloonKeyPressed(event, data)
#         redrawAllWrapper(canvas, data)
# 
#     def timerFiredWrapper(canvas, data):
#         balloonTimerFired(data)
#         redrawAllWrapper(canvas, data)
#         # pause, then call timerFired again
#         canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
#     # Set up data and call init
#     class Struct(object): pass
#     data = Struct()
#     data.width = width
#     data.height = height
#     data.timerDelay = 100 # milliseconds
#     root = Tk()
#     root.resizable(width=False, height=False) # prevents resizing window
#     balloonInit(data)
#     # create the root and the canvas
#     canvas = Canvas(root, width=data.width, height=data.height)
#     canvas.configure(bd=0, highlightthickness=0)
#     canvas.pack()
#     # set up events
#     root.bind("<Button-1>", lambda event:
#                             mousePressedWrapper(event, canvas, data))
#     root.bind("<Key>", lambda event:
#                             keyPressedWrapper(event, canvas, data))
#     timerFiredWrapper(canvas, data)
#     # and launch the app
#     root.mainloop()  # blocks until window is closed
#     print("bye!")
# 
# runBalloonGame(600, 400)