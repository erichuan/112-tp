'''
General animation framework taken from 112 course notes
'''
from tkinter import *
import random, os

orange1 = '''
a
b
c
d
'''
blue1 = '''
a
b
c
d
'''
green1 = '''
a
b
c
d
'''
gold1 = '''
a
b
c
d
'''
orange2 = '''
a
b
c
d
'''
blue2 = '''
a
b
c
d
'''
green2 = '''
a
b
c
d
'''
gold2 = '''
a
b
c
d
'''
orange3 = '''
a
b
c
d
'''
blue3 = '''
a
b
c
d
'''
green3 = '''
a
b
c
d
'''
gold3 = '''
a
b
c
d
'''
orange4 = '''
a
b
c
d
'''
blue4 = '''
a
b
c
d
'''
green4 = '''
a
b
c
d
'''
gold4 = '''
a
b
c
d
'''

row1 = [orange1, blue1, green1, gold1]
row2 = [orange2, blue2, green2, gold2]
row3 = [orange3, blue3, green3, gold3]
row4 = [orange4, blue4, green4, gold4]
trueColors = [row1, row2, row3, row4]


def init(data):
    loadPresidentImages(data) 
    data.margin = 45
    data.inBetween = 10
    data.trueColors = trueColors

def loadPresidentImages(data):
    data.presidents = ["andy", "cohon", "farnam", "subra"]
    data.presidentImages = []
    for president in data.presidents:
        filename = "presidents-gifs/%s.gif" % (president)
        data.presidentImages.append(PhotoImage(file=filename))

def drawChoices(canvas, data, tc):
    choice1 = canvas.create_rectangle(10, 225, 90,350)
    canvas.create_text(50, 287.5, text=data.trueColors[tc][0])
    choice2 = canvas.create_rectangle(100, 225, 190,350)
    canvas.create_text(145, 287.5, text=data.trueColors[tc][1])
    choice3 = canvas.create_rectangle(195, 225, 290,350)
    canvas.create_text(242.5, 287.5, text=data.trueColors[tc][2])
    choice4 = canvas.create_rectangle(300, 225, 390,350)
    canvas.create_text(345, 287.5, text=data.trueColors[tc][3])

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def timerFired(event):
    pass

def redrawAll(canvas, data):
    andy = canvas.create_image(data.margin+10, 150, image=data.presidentImages[0])
    cohon = canvas.create_image(data.margin+100, 150, image=data.presidentImages[1])
    farnam = canvas.create_image(data.margin+195, 150, image=data.presidentImages[2])
    subra = canvas.create_image(data.margin+300, 150, image=data.presidentImages[3])
    
    drawChoices(canvas, data, 0)
    
    

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

run(400,400)