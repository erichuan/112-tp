'''
General animation framework taken from 112 course notes
'''
from tkinter import *
import random, os

orange1 = '''
Active
Lively
Spontaneous
'''
blue1 = '''
Harmonious
Compassionate
Helpful
'''
green1 = '''
Versatile
Inventive
Competent
'''
gold1 = '''
Parental
Traditional
Responsible
'''
orange2 = '''
Competitive
Impactful
Negotiator
'''
blue2 = '''
Positive
Empathetic
Communicative
'''
green2 = '''
Curious
Conceptual
Knowledgeable
'''
gold2 = '''
Practical
Sensible
Dependable
'''
orange3 = '''
Realistic
Open-minded
Adventuresome
'''
blue3 = '''
Devoted
Warm
Emotional
'''
green3 = '''
Theoretical
Seeking
Ingenious
'''
gold3 = '''
Loyal
Conservative
Organized
'''
orange4 = '''
Daring
Impulsive
Fun
'''
blue4 = '''
Tender
Inspirational
Dramatic
'''
green4 = '''
Determined
Complex
Composed
'''
gold4 = '''
Concerned
Procedural
Cooperative
'''
orange5 = '''
Exciting
Courageous
Skillful
'''
blue5 = '''
Vivacious
Affectionate
Sympathetic
'''
green5 = '''
Philosophical
Principled
Rational
'''
gold5 = '''
Orderly
Conventional
Caring
'''

row1 = [orange1, gold1, blue1, green1]
row2 = [orange2, gold2, blue2, green2]
row3 = [orange3, gold3, blue3, green3]
row4 = [orange4, gold4, blue4, green4]
row5 = [orange5, gold5, blue5, green5]
trueColors = [row1, row2, row3, row4, row5]

orangeText = '''
As an ORANGE person

Your Leadership style: Expects quick action and immediate results; direct and
assertive; energetic; enthusiastic; creativity!!!

Ideal situation: someone else does the detail work; variety and challenge; 
relaxed; spontaneity; people intensive

Potential pitfalls: impulsive; limited follow through; neglects prep time; 
avoids problems rather than create thorough plan
'''

goldText = '''
As a GOLD person

Your Leadership style: respects hierarchy; detail oriented; rules and policies;
expects others to do the same; organizational structure; reliable

Ideal situation: Neat, orderly environment; security; steady, stable state;
routine schedule; sense of usefulness and belonging

Potential pitfalls: not as flexible as situation requires; assumes they know
best; likes status quo; doesn't understand need for change
'''

blueText = '''
AS a BLUE person

Your Leadership style: inspirational; appreciative; facilitative; emotional;
people-centered, relationships focused

Ideal situation: team focus; harmony; cooperation; support; process oriented;
time and space for reflection; non-competitive environment

Potential pitfalls: may be conflict-averse; too trusting; gullible; easily hurt;
too focused from pleasing others; blind loyalty
'''

greenText = '''
As a GREEN person

Your Leadership style: leads by analyzing goals; tough minded with others;
expert power; prefers autonomy

Ideal situation: independent thinking is valued; discussion and debate;
challenging; innovative; flexible

Potential pitfalls: makes others feel intellectually inadequate; too complex;
over-intellectualizes instructions; acts impersonally
'''

def trueColorsInit(data):
    loadPresidentImages(data) 
    data.margin = data.width//5
    data.inBetween = data.margin/6
    data.trueColors = trueColors
    # data.results = [([0]*4) for i in range(5)]
    data.results = [0]*4
    data.tc = 0
    data.choice1 = Choice(90, 175, 170, 300)
    data.choice2 = Choice(190, 175, 260, 300)
    data.choice3 = Choice(280, 175, 360, 300)
    data.choice4 = Choice(380, 175, 460, 300)
    data.showResults = False
    data.bestIndex = []
    data.colorMapping = {"orange": 0, "gold": 1, "blue": 2, "green": 3}
    data.colorTexts = {"orange": orangeText, "gold": goldText, "blue": blueText, "green": greenText}

def loadPresidentImages(data):
    data.presidents = ["andy", "cohon", "farnam", "subra"]
    data.presidentImages = []
    for president in data.presidents:
        filename = "presidents-gifs/%s.gif" % (president)
        data.presidentImages.append(PhotoImage(file=filename))
        
class Choice(object):
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.value = 0
    
    def drawBoxes(self, canvas, color):
        self.color = color
        canvas.create_rectangle(self.left, self.top, self.right, self.bottom, fill=self.color)
    
    def drawText(self, canvas, text):
        self.text = text
        midpt1 = (self.right-self.left)/2
        midpt2 = (self.bottom-self.top)/2
        canvas.create_text(self.left+midpt1, self.top+midpt2,text=self.text, font="Arial 12")

def drawChoices(canvas, data):
    data.choice1.drawBoxes(canvas, None)
    data.choice1.drawText(canvas, data.trueColors[data.tc][0])
    
    data.choice2.drawBoxes(canvas, None)
    data.choice2.drawText(canvas, data.trueColors[data.tc][1])

    data.choice3.drawBoxes(canvas, None)
    data.choice3.drawText(canvas, data.trueColors[data.tc][2])
    
    data.choice4.drawBoxes(canvas, None)
    data.choice4.drawText(canvas, data.trueColors[data.tc][3])

def getBestIndex(data):
    maxScore = 0
    for i in range(len(data.results)):
        if data.results[i] > maxScore:
            maxScore = data.results[i]
            data.bestIndex = [i]
        elif data.results[i] == maxScore:
            data.bestIndex.append(i)
    return data.bestIndex

def getPrimaryColor(data):
    primary = []
    
    if len(data.bestIndex) == 1:
        for color in data.colorMapping:
            if data.colorMapping[color] == data.bestIndex[0]:
                primary = [color]
    else:
        for index in data.bestIndex:
            for color in data.colorMapping:
                if data.colorMapping[color] == index:
                    primary.append(color)
    
    return primary

def drawResults(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="cyan")
    
    bestIndex = getBestIndex(data)
    bestColor = getPrimaryColor(data)
    primeColor = ""
    result1 = "Your PRIMARY Color(s) is/are  "
    colorAnalysis = ''''''
    colorAnalyses = ''''''

    if len(bestColor) == 1:
        primeColor = bestColor[0]
        result1 += primeColor
        colorAnalysis = data.colorTexts[primeColor]
    elif len(bestColor) > 2:
        bestColor = bestColor[:2]
        for color in bestColor:
            primeColor += color
            primeColor += ", "
            colorAnalyses += data.colorTexts[color]
            colorAnalyses += "\n"
        result1 += primeColor[:-2]
        colorAnalysis += colorAnalyses[:-1]
    else:
        for color in bestColor:
            primeColor += color
            primeColor += ", "
            colorAnalyses += data.colorTexts[color]
            colorAnalyses += "\n"
        result1 += primeColor[:-2]
        colorAnalysis += colorAnalyses[:-1]
            
    canvas.create_text(data.width/2, data.height*.15, text=result1)
    canvas.create_text(data.width/2, data.height/2, text=colorAnalysis,font="Arial 10")
   

def trueColorsMousePressed(event, data):
    if data.tc < 4:
        if (data.choice1.left <= event.x <= data.choice1.right) and (data.choice1.top <= event.y <= data.choice1.bottom):
            data.results[0] += 4
        elif (data.choice2.left <= event.x <= data.choice2.right) and (data.choice2.top <= event.y <= data.choice2.bottom):
            data.results[1] += 4
        elif (data.choice3.left <= event.x <= data.choice3.right) and (data.choice3.top <= event.y <= data.choice3.bottom):
            data.results[2] += 4
        elif (data.choice4.left <= event.x <= data.choice4.right) and (data.choice4.top <= event.y <= data.choice4.bottom):
            data.results[3] += 4
    
        data.tc += 1
    else:
        data.showResults = True
    
    if data.showResults:
        if (data.width*.75 <= event.x <= data.width*.95)  and (data.height*.85 <= event.y <= data.height*.95):
            data.showResults = False
            trueColorsInit(data)
    

def trueColorsKeyPressed(event, data):
    if event.keysym == "m":
        data.mode = "mainLoop"

def trueColorsTimerFired(event):
    pass

def trueColorsRedrawAll(canvas, data):
    if not data.showResults:
        canvas.create_rectangle(0,0,data.width,data.height,fill="cyan")
        
        andy = canvas.create_image(data.margin+10, data.height/4, image=data.presidentImages[0])
        cohon = canvas.create_image(data.margin+100, data.height/4, image=data.presidentImages[1])
        farnam = canvas.create_image(data.margin+195, data.height/4, image=data.presidentImages[2])
        subra = canvas.create_image(data.margin+300, data.height/4, image=data.presidentImages[3])
        
        drawChoices(canvas, data)
        
        canvas.create_text(data.width/2, data.height*.95, text="Hit 'm' to go back", fill="black")
    
    # draw results
    else:
        canvas.create_rectangle(0,0,data.width,data.height,fill="cyan")
        drawResults(canvas, data)
        
        canvas.create_rectangle(data.width*.75, data.height*.85, data.width*.95, data.height*.95, fill="red")
        canvas.create_text(data.width*.85, data.height*.9, text="Play Again", fill="white")
        canvas.create_text(data.width*.2, data.height*.95, text="Press 'm' to return to main loop")
    
    

####################################
# use the run function as-is
####################################

# def run(width=300, height=300):
#     def redrawAllWrapper(canvas, data):
#         canvas.delete(ALL)
#         canvas.create_rectangle(0, 0, data.width, data.height,
#                                 fill='white', width=0)
#         trueColorsRedrawAll(canvas, data)
#         canvas.update()    
# 
#     def mousePressedWrapper(event, canvas, data):
#         trueColorsMousePressed(event, data)
#         redrawAllWrapper(canvas, data)
# 
#     def keyPressedWrapper(event, canvas, data):
#         trueColorsKeyPressed(event, data)
#         redrawAllWrapper(canvas, data)
# 
#     def timerFiredWrapper(canvas, data):
#         trueColorsTimerFired(data)
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
#     trueColorsInit(data)
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
# run(600,400)