'''
General animation framework taken from animation demo notes
'''
from tkinter import *

####################################
# init
####################################

def init(data):
    # There is only one init, not one-per-mode
    data.mode = "homeScreen"

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "homeScreen"):    homeScreenMousePressed(event, data)
    elif (data.mode == "mainLoop"):    mainLoopMousePressed(event, data)
    elif (data.mode == "balloonGame"): balloonGameMousePressed(event, data) 
    elif (data.mode == "help"):        helpMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "homeScreen"):    homeScreenKeyPressed(event, data)
    elif (data.mode == "mainLoop"):    mainLoopKeyPressed(event, data)
    elif (data.mode == "balloonGame"): balloonGameKeyPressed(event, data)
    elif (data.mode == "help"):        helpKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "homeScreen"):    homeScreenTimerFired(data)
    elif (data.mode == "mainLoop"):    mainLoopTimerFired(data)
    elif (data.mode == "balloonGame"): balloonGameTimerFired(data)
    elif (data.mode == "help"):        helpTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "homeScreen"):    homeScreenRedrawAll(canvas, data)
    elif (data.mode == "mainLoop"):    mainLoopRedrawAll(canvas, data)
    elif (data.mode == "balloonGame"): balloonGameRedrawAll(canvas, data)
    elif (data.mode == "help"):        helpRedrawAll(canvas, data)

####################################
# homeScreen mode
####################################

def homeScreenMousePressed(event, data):
    pass

def homeScreenKeyPressed(event, data):
    if (event.keysym == "i"):
        data.mode = "help"
    elif (event.keysym == "m"):
        data.mode = "mainLoop"
    elif (event.keysym == "b"):
        data.mode = "balloonGame"

def homeScreenTimerFired(data):
    pass

def homeScreenRedrawAll(canvas, data):
    homeText = '''
    Welcome to Eric's 112 TP homescreen!
    It will be a create your own adventure interactive game.
    You will be faced with different scenarios where you will be able to make 
    decisions about what the circumstances are, how you would react, and other 
    sorts of cool decisions. You may also have to complete some activities in 
    order to advance in the narrative. In the end, your decisions will be compiled, 
    summarized, and analyzed based on organizational behavior theory as well as 
    learn about your strengths, weaknesses as a leader and what you can do.
    
    Press "i" for general instructions!
    Press "m" for the main loop!
    Press "b" for the balloon game!
    Use spacebar to navigate through the adventure throughout!
    '''
    canvas.create_text(data.width//2, data.height//2, text=homeText,font="Arial 12")

####################################
# help mode
####################################

def helpMousePressed(event, data):
    pass

def helpKeyPressed(event, data):
    if (event.keysym == "h"):
        data.mode = "homeScreen"
    elif (event.keysym == "m"):
        data.mode = "mainLoop"
    elif (event.keysym == "b"):
        data.mode = "balloonGame"

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    helpText = '''
    Welcome to the future of the general instructions page!
    
    Press "h" to return to home screen
    Press "m" for the main loop!
    Press "b" for the balloon game!
    Use spacebar to navigate through the adventure throughout!
    '''
    canvas.create_text(data.width//2, data.height//2, text=helpText)

####################################
# mainLoop mode
####################################
# ask about how to keep clicking for things to come out sequentially
# multiple things to happen for elif.keysym == "space"
# might be MVC violation since there'll be a draw function in keyPressed?

def mainLoopMousePressed(event, data):
    pass

def mainLoopKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.mode = "homeScreen"
    elif (event.keysym == 'i'):
        data.mode = "help"
    elif (event.keysym == "b"):
        data.mode = "balloonGame"
    elif (event.keysym == "space"):
        # drawBubble(canvas, data)
        pass

def mainLoopTimerFired(data):
    pass

def mainLoopRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width, data.height,fill="lime")
    
    canvas.create_oval(data.width//5-40, data.height//2-100,
                       data.width//5+40, data.height//2+100,
                       fill="black")
    
    speechbubble1 = '''
    Today is your first day at 15-112 Inc as our newest intern.
    We can't wait to meet you, and so do your colleagues as well.
    
    Your time during this internship, however, will be challenging.
    But you will learn new things; you will learn things about yourself.
    Without further ado, let's begin!
    '''
    canvas.create_text(data.width//2, data.height//4, text=speechbubble1)
    
    placeholderText = '''
    # This will be the bulk of the adventure will take place. There will be
    animations, games, and other fun stuff. Maybe there'll be a maze? We'll see
    as Eric progresses through TP1, TP2, and TP3.
    
    Press "i" for general instructions!
    Press "h" to return to the home screen!
    Press "b" for the balloon game! 
    '''
    canvas.create_text(data.width/2, data.height*0.8, text=placeholderText)

####################################
# balloonGame mode
####################################
# ask how to embed game into a 'mode' (as a another 'frame' in the entire story)

def balloonGameMousePressed(event, data):
    pass

def balloonGameKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.mode = "homeScreen"
    elif (event.keysym == 'i'):
        data.mode = "help"
    elif (event.keysym == 'm'):
        data.mode = "mainLoop"

def balloonGameTimerFired(data):
    pass

def balloonGameRedrawAll(canvas, data):
    moreText = '''
    This is where ONE of the games, the balloonGame, will take place!
    It's based on the Balloon Analog Risk Test (BART), a behavioral test 
    of risk assessment (Lejuez et al., 2002).
    
    Press "i" for general instructions!
    Press "h" to return to the home screen!
    Press "m" for the main loop! 
    '''
    canvas.create_text(data.width//2, data.height//2, text=moreText)


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
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

run(500, 500)