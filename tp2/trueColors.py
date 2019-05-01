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


def trueColorsInit(data):
    loadPresidentImages(data) 
    data.margin = data.width//5
    data.inBetween = data.margin/6
    data.trueColors = trueColors
    data.results = [([None]*4) for i in range(5)]
    data.tc = 0
    data.choice1 = Choice(90, 175, 170, 300)
    data.choice2 = Choice(190, 175, 260, 300)
    data.choice3 = Choice(280, 175, 360, 300)
    data.choice4 = Choice(380, 175, 460, 300)
    data.tmpLst = []

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
    
    def drawBoxes(self, canvas, color):
        self.color = color
        canvas.create_rectangle(self.left, self.top, self.right, self.bottom, fill=self.color)
    
    def drawText(self, canvas, text):
        self.text = text
        midpt1 = (self.right-self.left)/2
        midpt2 = (self.bottom-self.top)/2
        canvas.create_text(self.left+midpt1, self.top+midpt2,text=self.text, font="Arial 12")
    
    def isClicked(self, x, y):
        self.x = x
        self.y = y
        return (self.left <= x <= self.right) and (self.top <= y <= self.bottom)

def drawChoices(canvas, data):
    data.choice1.drawBoxes(canvas, None)
    data.choice1.drawText(canvas, data.trueColors[data.tc][0])
    
    data.choice2.drawBoxes(canvas, None)
    data.choice2.drawText(canvas, data.trueColors[data.tc][1])

    data.choice3.drawBoxes(canvas, None)
    data.choice3.drawText(canvas, data.trueColors[data.tc][2])
    
    data.choice4.drawBoxes(canvas, None)
    data.choice4.drawText(canvas, data.trueColors[data.tc][3])

def trueColorsMousePressed(event, data):
    if data.choice1.isClicked(event.x, event.y):
        data.tmpLst.append(0)
    elif data.choice2.isClicked(event.x, event.y):
        data.tmpLst.append(1)
    elif data.choice3.isClicked(event.x, event.y):
        data.tmpLst.append(2)
    elif data.choice4.isClicked(event.x, event.y):
        data.tmpLst.append(3)
    
    num = 4
    for item in data.tmpLst:
        data.results[data.tc][item] = num
        num -= 1
    
    num = 4
    
    if ((None not in data.results[data.tc]) and (data.tc < len(data.trueColors))):
        data.tc += 1
        
    
    print(data.results)

def trueColorsKeyPressed(event, data):
    if event.keysym == "m":
        data.mode = "mainLoop"

def trueColorsTimerFired(event):
    pass

def trueColorsRedrawAll(canvas, data):
    andy = canvas.create_image(data.margin+10, data.height/4, image=data.presidentImages[0])
    cohon = canvas.create_image(data.margin+100, data.height/4, image=data.presidentImages[1])
    farnam = canvas.create_image(data.margin+195, data.height/4, image=data.presidentImages[2])
    subra = canvas.create_image(data.margin+300, data.height/4, image=data.presidentImages[3])
    
    drawChoices(canvas, data)
    

####################################
# use the run function as-is
####################################

# def run(width=300, height=300):
#     def redrawAllWrapper(canvas, data):
#         canvas.delete(ALL)
#         canvas.create_rectangle(0, 0, data.width, data.height,
#                                 fill='white', width=0)
#         redrawAll(canvas, data)
#         canvas.update()    
# 
#     def mousePressedWrapper(event, canvas, data):
#         mousePressed(event, data)
#         redrawAllWrapper(canvas, data)
# 
#     def keyPressedWrapper(event, canvas, data):
#         keyPressed(event, data)
#         redrawAllWrapper(canvas, data)
# 
#     def timerFiredWrapper(canvas, data):
#         timerFired(data)
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
#     init(data)
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