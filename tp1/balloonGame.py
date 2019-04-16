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
    data.currTotal = 0
    data.runningTotal = 0
    data.clicks = 0
    data.clickList = []
    data.tolerance = []
    for i in range(30):
        tolerance = random.randint(1,32)
        data.tolerance.append(tolerance)
    
    data.isPopped = False
    data.cx = data.width/2
    data.cy = data.height*0.4
    data.hPlus = 0
    data.vPlus = 0
    data.balloons = []
    

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

def playGameMousePressed(event, data):
    index = 0
    while index < len(data.tolerance):
        if ((data.width*0.075 <= event.x <= data.width*0.325) and 
            (data.height*0.79 <= event.y <= data.height*0.91)):
            data.runningTotal += data.currTotal
        
        if data.clicks <= data.tolerance[index]:
            if ((data.width*0.375 <= event.x <= data.width*0.625) and 
                (data.height*0.79 <= event.y <= data.height*0.91)):
                data.hPlus += 10
                data.vPlus += 25
                data.clicks += 1
        else:
            data.isPopped = not data.isPopped
            data.clickList.append(data.clicks)
            data.balloons.append((data.hPlus, data.vPlus))
            data.clicks = data.hPlus = data.vPlus = 0
            data.isPopped = not data.isPopped
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
                       text="Current Earnings:" + str(data.currTotal),
                       anchor="nw")
    canvas.create_text(data.width*0.7,data.height*0.85,
                       text="Cumulative Earnings:" + str(data.runningTotal),
                       anchor="sw")
    # draw balloon
    if data.isPopped == False:
        canvas.create_oval(data.cx-data.hPlus,data.cy-data.vPlus,
                            data.cx+data.hPlus,data.cy+data.vPlus,
                            fill="red", outline="black")
    else:
        pass

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