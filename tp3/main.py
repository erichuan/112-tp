'''
General animation framework taken from animation demo notes:
https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html

Ball bounce code adapted from that of the course notes
'''
from tkinter import *
from othello import *
from conflictResolutionStyles import *
from balloonGame import *
from trueColors import *

####################################
# init
####################################

def init(data):
    # There is only one init, not one-per-mode
    data.mode = "landingPage"
    othelloInit(data)
    loadmentors(data)
    winWinWinInit(data)
    balloonInit(data)
    trueColorsInit(data)
    
    # home page animation
    loadImages(data)
    data.dwight = data.preparedImages[1]
    data.dwightX = random.randint(data.dwight.width(), data.width - data.dwight.width())
    data.dwightY = random.randint(data.dwight.height(), data.height - data.dwight.height())
    data.speedX = 2
    data.speedY = 2
    data.timerDelay = 20
    data.timer = 0
    data.refer = False
    
    # balloonSplashScreen
    data.yeet = False

def loadImages(data):
    data.images = ["mscottSHIP", "dwight"]
    data.preparedImages = []
    for img in data.images:
        filename = "office-gifs/%s.gif" % (img)
        data.preparedImages.append(PhotoImage(file=filename))

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "landingPage"):            landingPageMousePressed(event, data)
    elif (data.mode == "mainScreen"):           mainScreenMousePressed(event, data)
    elif (data.mode == "mainLoop"):             mainLoopMousePressed(event, data)
    elif (data.mode == "winSplashScreen"):      winSplashScreenMousePressed(event, data)
    elif (data.mode == "winWinWin"):            winWinWinMousePressed(event, data)
    elif (data.mode == "balloonSplashScreen"):  balloonSplashScreenMousePressed(event, data)
    elif (data.mode == "balloon"):              balloonMousePressed(event, data)
    elif (data.mode == "othelloSplashScreen"):  othelloSplashScreenMousePressed(event, data)
    elif (data.mode == "othello"):              othelloMousePressed(event, data)
    elif (data.mode == "trueColors"):           trueColorsMousePressed(event, data)
    elif (data.mode == "endGame"):              endGameMousePressed(event, data) 

def keyPressed(event, data):
    if (data.mode == "landingPage"):            landingPageKeyPressed(event, data)
    elif (data.mode == "mainScreen"):           mainScreenKeyPressed(event, data)
    elif (data.mode == "mainLoop"):             mainLoopKeyPressed(event, data)
    elif (data.mode == "winSplashScreen"):      winSplashScreenKeyPressed(event, data)
    elif (data.mode == "winWinWin"):            winWinWinKeyPressed(event, data)
    elif (data.mode == "balloonSplashScreen"):  balloonSplashScreenKeyPressed(event, data)
    elif (data.mode == "balloon"):              balloonKeyPressed(event, data)
    elif (data.mode == "othelloSplashScreen"):  othelloSplashScreenKeyPressed(event, data)
    elif (data.mode == "othello"):              othelloKeyPressed(event, data)
    elif (data.mode == "trueColors"):           trueColorsKeyPressed(event, data)
    elif (data.mode == "endGame"):              endGameKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "landingPage"):            landingPageTimerFired(data)
    elif (data.mode == "mainScreen"):           mainScreenTimerFired(data)
    elif (data.mode == "mainLoop"):             mainLoopTimerFired(data)
    elif (data.mode == "winSplashScreen"):      winSplashScreenTimerFired(data)
    elif (data.mode == "winWinWin"):            winWinWinTimerFired(data)
    elif (data.mode == "balloonSplashScreen"):  balloonSplashScreenTimerFired(data)
    elif (data.mode == "balloon"):              balloonTimerFired(data)
    elif (data.mode == "othelloSplashScreen"):  othelloSplashScreenTimerFired(data)
    elif (data.mode == "othello"):              othelloTimerFired(data)
    elif (data.mode == "trueColors"):           trueColorsTimerFired(data)
    elif (data.mode == "endGame"):              endGameTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "landingPage"):            landingPageRedrawAll(canvas, data)
    elif (data.mode == "mainScreen"):           mainScreenRedrawAll(canvas, data)
    elif (data.mode == "mainLoop"):             mainLoopRedrawAll(canvas, data)
    elif (data.mode == "winSplashScreen"):      winSplashScreenRedrawAll(canvas, data)
    elif (data.mode == "winWinWin"):            winWinWinRedrawAll(canvas, data)
    elif (data.mode == "balloonSplashScreen"):  balloonSplashScreenRedrawAll(canvas, data)
    elif (data.mode == "balloon"):              balloonRedrawAll(canvas, data)
    elif (data.mode == "othelloSplashScreen"):  othelloSplashScreenRedrawAll(canvas, data)
    elif (data.mode == "othello"):              othelloRedrawAll(canvas, data)
    elif (data.mode == "trueColors"):           trueColorsRedrawAll(canvas, data)
    elif (data.mode == "endGame"):              endGameRedrawAll(canvas, data)

####################################
# landingPage mode
####################################

def landingPageMousePressed(event, data):
    if ((data.width*.4 <= event.x <= data.width*.6) and (data.height*.6 <= event.y <= data.height*.7)):
        data.mode = "mainScreen"

def landingPageKeyPressed(event, data):
    pass

def ballMovement(data):
    data.dwightX += data.speedX
    data.dwightY += data.speedY 
       
    # Bounce Feature
    if data.dwightX >= data.width:
        data.speedX = -abs(data.speedX)
    elif data.dwightX <= 0:
        data.speedX = abs(data.speedX)
    elif data.dwightY <= 0:
        data.speedY = abs(data.speedY)
    elif data.dwightY >= data.height:
        data.speedY = -abs(data.speedY)

def landingPageTimerFired(data):
    ballMovement(data)

def landingPageRedrawAll(canvas, data):
    # background
    canvas.create_rectangle(0,0,data.width, data.height,fill="purple", width=0)
    
    # title
    canvas.create_rectangle(data.width/5,data.height/10,data.width*.8,data.height*.4,fill="red")
    canvas.create_text(data.width/3, data.height*.16, text="BE an", font="Arial 20", anchor="e", fill="white") 
    canvas.create_text(data.width*.24, data.height*.24, text="EMERGING", font="Arial 30 bold", anchor="w", fill="lime") 
    canvas.create_text(data.width*.53, data.height*.24, text="Leader", font="Arial 30", anchor="w", fill="white")
    tagline = "All aboard the leadership ride and learn something about yourself!"
    canvas.create_text(data.width/2, data.height/3, text=tagline, font="Arial 12 italic", fill="cyan")
    
    # start button
    canvas.create_rectangle(data.width*.4, data.height*.6, data.width*.6, data.height*.7, fill="lime")
    canvas.create_text(data.width/2, data.height*.65, text="Start", fill="white")
    
    # bouncing dwight
    canvas.create_image(data.dwightX, data.dwightY, image=data.preparedImages[1])
                       
    
    # canvas.create_image(data.width/4, data.height*.7, image=data.preparedImages[0])
    
    homeText = '''
    Welcome to Eric's 112 TP homescreen!
    It will be a create your own adventure interactive game.
    You will be faced with different scenarios where you will be able to make 
    decisions about what the circumstances are, how you would react, and other 
    sorts of cool decisions. You may also have to complete some activities in 
    order to advance in the narrative. In the end, your decisions will be compiled, 
    summarized, and analyzed based on organizational behavior theory as well as 
    learn about your strengths, weaknesses as a leader and what you can do.
    
    '''
    # canvas.create_text(data.width/2, data.height*.75, text=homeText,font="Arial 12", fill="white")

####################################
# mainScreen mode
####################################

def mainScreenMousePressed(event, data):
    if ((data.width*.15 <= event.x <= data.width/2) and 
        (data.height*.3 <= event.y <= data.height*.6)):
        data.mode = "mainLoop"

def mainScreenKeyPressed(event, data):
    pass

def mainScreenTimerFired(data):
    pass

def mainScreenRedrawAll(canvas, data):
    # background
    canvas.create_rectangle(0,0,data.width,data.height,fill="purple")
    
    # story 1
    canvas.create_text(data.width/2, data.height/5, text="Choose a story", fill="white", font="Arial 30")
    canvas.create_image(data.width*.3, data.height/2,image=data.preparedImages[0])
    canvas.create_text(data.width*.3, data.height*.72, text="All aboard the leaderSHIP!", fill="white", font="Arial 15")
    
    # (future) story 2
    canvas.create_rectangle(data.width*.6, data.height/3, data.width*.85, data.height*.65,fill="red")
    canvas.create_text(data.width*.72, data.height*.72, text="TBD", fill="white", font="Arial 20")
    

####################################
# mainLoop mode
####################################
# ask about how to keep clicking for things to come out sequentially
# multiple things to happen for elif.keysym == "space"
# might be MVC violation since there'll be a draw function in keyPressed?

def mainLoopMousePressed(event, data):
    if ((data.width*.05 <= event.x <= data.width*.4) and 
        (data.height*.93-15 <= event.y <= data.height*.93+15)):
        data.refer = True
    
    if data.refer == True:
        if ((data.width*.1 <= event.x <= data.width*.9) and 
            (data.width*.15 <= event.y <= data.width*.75)):
            data.refer = False
    
    if ((data.width*.36 <= event.x <= data.width*.58) and 
        (data.height*.75 <= event.y <= data.height*.85)):
        data.mode = "winSplashScreen"
    
    elif ((data.width*.08 <= event.x <= data.width*.3) and 
          (data.height*.75 <= event.y <= data.height*.85)):
        data.mode = "balloonSplashScreen"
    
    elif ((data.width*.64 <= event.x <= data.width*.86) and 
          (data.height*.75 <= event.y <= data.height*.85)):
        data.mode = "trueColors"
    elif ((data.width*.6 <= event.x <= data.width*.9) and 
          (data.height*.93-15 <= event.y <= data.height*.93+15)):
        data.mode = "othelloSplashScreen"

def mainLoopKeyPressed(event, data):
    if event.keysym == "Left":
        data.mode = "mainScreen"
    elif event.keysym == "Escape":
        data.mode = "endGame"

def mainLoopTimerFired(data):
    pass

def mainLoopRedrawAll(canvas, data):
    # background
    canvas.create_rectangle(0,0,data.width, data.height,fill="azure")
    
    speechbubble1 = '''
    Welcome aboard the USS Dunder Mifflin - Leader SHIP!
    
    Today is you embark on your first day at the Michael Scott Paper 
    Company II as our newest intern. We can't wait to meet you, and 
    so do your colleagues as well.
    
    However, unlike past interns (temps) at this company, your time 
    at this internship will be challenging. You will learn new things; 
    you will learn things about yourself. And in the end, you will come
    out the program an 'emerged leader'.
    
    Without further ado, let's begin!
    
    Hit 'left arrow' to go back
    Press 'Escape' to exit game
    '''
    canvas.create_text(data.width//2, data.height//3, text=speechbubble1)
    
    # buttons
    riskButton = canvas.create_rectangle(data.width*.08, data.height*.75, data.width*.3, data.height*.85, fill="red")
    canvas.create_text(data.width*.19, data.height*.8, text="DARE TO TAKE RISKS", fill="white", font="Arial 11")
    
    resolveButton = canvas.create_rectangle(data.width*.36, data.height*.75, data.width*.58, data.height*.85, fill="green")
    canvas.create_text(data.width*.47, data.height*.8, text="MEND THE WOUNDS", fill="white", font="Arial 11")
    
    trueColorsButton = canvas.create_rectangle(data.width*.64, data.height*.75, data.width*.86, data.height*.85, fill="blue")
    canvas.create_text(data.width*.75, data.height*.8, text="FIND YOUR TRUE COLORS", fill="white", font="Arial 9")
    
    # secret challenge (othello)
    plusChallenge = canvas.create_rectangle(data.width*.6, data.height*.93-15, data.width*.9, data.height*.93+15, fill="purple")
    dunderCode = '''
    the Dunder Code!
    Challenge Against an AI!
    '''
    canvas.create_text(data.width*.75, data.height*.93, text=dunderCode,fill="white", font="Arial 10")
    
    # references
    canvas.create_rectangle(data.width*.05, data.height*.93-15, data.width*.2, data.height*.93+15, fill="yellow")
    canvas.create_text(data.width*.12, data.height*.93, text="References")
    
    if data.refer == True:
        references = '''
        The following activities are based on existing leadership/personality 
        assessments based on organizational behavior theory.
        
        "Dare to Take Risks": Balloon Analog Risk Test (BART), behavioral test 
        of risk assessment (Lejuez et al., 2002)
        
        "Mend the Wounds": Conflict Management Styles Assessment,
        “Conflict and Negotiation Processes in Organizations”
        
        "Find your True Colors": Don Lowry's "True Colors" Personality Assessment
        (1978) and based on Carnegie Mellon's Emerging Leaders version of 
        "True Colors" activity
        '''
        canvas.create_rectangle(data.width*.1, data.height*.15, data.width*.9, data.height*.75, fill="yellow")
        canvas.create_text(data.width/2, data.height*.45, text=references, font="Arial 11")
        
####################################
# winSplashScreen mode
####################################
def loadmentors(data):
    data.mentorLst = ["resolute", "michaelPhyllis", "elmentors"]
    data.preparedMentors = []
    for img in data.mentorLst:
        filename = "office-gifs/%s.gif" % (img)
        data.preparedMentors.append(PhotoImage(file=filename))

def winSplashScreenMousePressed(event, data):
    if ((data.width*.4 <= event.x <= data.width*.6) and (data.height/2-15 <= event.y <= data.height/2+15)):
        data.mode = "winWinWin"

def winSplashScreenKeyPressed(event, data):
    if event.keysym == "m":
        data.mode = "mainLoop"

def winSplashScreenTimerFired(data):
    pass

def winSplashScreenRedrawAll(canvas, data):
    # background
    canvas.create_rectangle(0,0,data.width,data.height,fill="beige")
    
    # title
    canvas.create_rectangle(data.width/5,data.height/10,data.width*.8,data.height*.4,fill="lime")
    canvas.create_text(data.width/2, data.height/4, text="What's your conflict resolution style?", fill="blue", font="Arial 18 bold")
    
    canvas.create_image(data.width*.15, data.height*.75, image=data.preparedMentors[0])
    canvas.create_image(data.width/2, data.height*.75, image=data.preparedMentors[1])
    canvas.create_image(data.width*.85, data.height*.75, image=data.preparedMentors[2])
    
    # start button
    canvas.create_rectangle(data.width*.4, data.height/2-15, data.width*.6, data.height/2+15, fill="red")
    canvas.create_text(data.width/2, data.height/2, text="Start", fill="white")
    
    canvas.create_text(data.width/2, data.height*.95, text="Hit 'm' to go back", fill="black")

####################################
# balloonSplashScreen mode
####################################
def balloonSplashScreenMousePressed(event, data):
    if ((data.width*0.375 <= event.x <= data.width*0.625) and 
        (data.height*0.69 <= event.y <= data.height*0.81)):
        data.mode = "balloon"

def balloonSplashScreenKeyPressed(event, data):
    if event.keysym == "m":
        data.mode = "mainLoop"

def balloonSplashScreenTimerFired(data):
    pass

def balloonSplashScreenRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="dark orange")
    canvas.create_rectangle(data.width/4, data.height*.1, 3*data.width/4, data.height*.3,fill="lime")
    canvas.create_text(data.width/2, data.height/5, text="Dare you to take risks!", fill="purple", font="Arial 20 bold")
    
    introText = '''
    Maximize the amount of money you can make 
    while minimizing the amount of balloons popped!
    
    You only earn points for "realized" gains, meaning the
    balloon does not pop.
    
    Hit "Start" to start game!
    Good luck!
    '''
    canvas.create_text(data.width/2, data.height/2, text=introText)
    
    # start button
    canvas.create_rectangle(data.width*0.375, data.height*0.69, 
                            data.width*0.625, data.height*0.81,
                            fill="red")
    canvas.create_text(data.width/2, data.height*0.75,text="Start",
                       fill="yellow")
                       
    canvas.create_text(data.width/2, data.height*.95, text="Hit 'm' to go back", fill="black")

####################################
# othelloSplashScreen mode
####################################

def othelloSplashScreenMousePressed(event, data):
    pass

def othelloSplashScreenKeyPressed(event, data):
    if event.keysym == "o":
        data.mode = "othello"
    elif event.keysym == "m":
        data.mode = "mainLoop"

def othelloSplashScreenTimerFired(data):
    pass

def othelloSplashScreenRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="beige")
    
    moreText = '''
    The professional world can be like a game of Othello.
        
    The professional world can be a competitive place. While teams and the 
    collective generally allow one to be more effective as well as allow for
    access to more diverse information, it is important for the individual to
    be productive assertive themselves. 
    
    As such, all incoming employees of Dunder Mifflin have gone through a game of
    Othello, not only to train one's strategic mindset but also in the end, if
    successful to experience the feeling of dominance over the game baord, and
    if unsuccessful to reflect upon the experience and learn from one's mistakes.
    

    Press "m" for the main loop! 
    Press "o" to begin game!
    '''
    canvas.create_text(data.width//2, data.height//2, text=moreText, font="Arial 12")

####################################
# endGame mode
####################################

def endGameMousePressed(event, data):
    if ((data.width*.3 <= event.x <= data.width*.6) and 
        (data.height*.7 <= event.y <= data.height*.8)):
        data.mode = "landingPage"

def endGameKeyPressed(event, data):
    pass

def endGameTimerFired(data):
    pass

def endGameRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="black")
    
    endText = '''
    THANK YOU FOR PLAYING. HOPE YOU LEARNED SOMETHING ABOUT 
    LEADERSHP AND ABOUT YOURSELF. LOOK FORWARD TO NEW ADVENTURES 
    COMING SOON TO YOUR NEXT 15112 CLASS!
    '''
    canvas.create_text(data.width//2, data.height//2, text=endText, font="Roboto 15", fill="yellow")
    
    landingText = '''
    Press here to return to home page!
    '''
    canvas.create_text(data.width//2, data.height*.75, text=landingText, font="Roboto 15", fill="yellow")

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

run(600, 400)