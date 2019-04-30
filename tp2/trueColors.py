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


def init(data):
    loadPresidentImages(data) 
    data.margin = 45
    data.inBetween = 10
    data.trueColors = trueColors
    data.results = [([0]*4) for i in range(4)]
    data.tc = 0

def loadPresidentImages(data):
    data.presidents = ["andy", "cohon", "farnam", "subra"]
    data.presidentImages = []
    for president in data.presidents:
        filename = "presidents-gifs/%s.gif" % (president)
        data.presidentImages.append(PhotoImage(file=filename))

def drawChoices(canvas, data):
    choice1 = canvas.create_rectangle(10, 225, 90,350)
    canvas.create_text(50, 287.5, text=data.trueColors[data.tc][0])
    choice2 = canvas.create_rectangle(100, 225, 190,350)
    canvas.create_text(145, 287.5, text=data.trueColors[data.tc][1])
    choice3 = canvas.create_rectangle(195, 225, 290,350)
    canvas.create_text(242.5, 287.5, text=data.trueColors[data.tc][2])
    choice4 = canvas.create_rectangle(300, 225, 390,350)
    canvas.create_text(345, 287.5, text=data.trueColors[data.tc][3])

def mousePressed(event, data):
    if data.tc < len(data.trueColors):
        if ((10 <= event.x <= 90) and (225 <= event.y <= 350)):
            data.results[data.tc][0] += 4
        elif ((100 <= event.x <= 190) and (225 <= event.y <= 350)):
            data.results[data.tc][1] += 4
        elif ((195 <= event.x <= 290) and (225 <= event.y <= 350)):
            data.results[data.tc][2] += 4
        elif ((300 <= event.x <= 390) and (225 <= event.y <= 350)):
            data.results[data.tc][3] += 4
        
        data.tc += 1

def keyPressed(event, data):
    pass

def timerFired(event):
    pass

def redrawAll(canvas, data):
    andy = canvas.create_image(data.margin+10, 150, image=data.presidentImages[0])
    cohon = canvas.create_image(data.margin+100, 150, image=data.presidentImages[1])
    farnam = canvas.create_image(data.margin+195, 150, image=data.presidentImages[2])
    subra = canvas.create_image(data.margin+300, 150, image=data.presidentImages[3])
    
    drawChoices(canvas, data)
    
    

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

run(600,400)