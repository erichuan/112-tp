'''
General animation framework taken from 112 course notes
'''
from tkinter import *
import random

initPrompts = '''
1. I enjoy digging into the issues to find solutions that work for everybody.
2. I do my best to negotiate a “give-and-take” approach to conflict.
3. I believe it’s important to keep relationships civil and associates happy.
4. It’s important to argue my case well to convince the other person of the
merits of my position.
5. In times of conflict, I gather as many facts as I can to keep the
conversation productive.
6. In a conflict situation, I am calm and collected and usually leave as soon
as possible.
7. I approach conflict from both sides of the argument. What are my
needs? What will work for the other person? What are the actual
issues?
8. My preferred way of dealing with conflict is to compromise and move
past the discomfort.
9. Often, I enjoy conflict. It is challenging and allows me to engage my
intellect.
10. Conflict makes me feel stressed and anxious.
11. Friends and family are everything to me, so I often accommodate their
point of view.
12. When I see an obvious solution, I argue my case strongly.
13. If it comes to a stand off, I will meet people halfway.
14. Keeping the peace is my priority. I don’t like tension.
15. When I have bad feelings about someone, I keep them to myself.
'''
promptList = []
for line in initPrompts.splitlines():
    if line == "":
        continue
    if line[0].isdigit():
        promptList.append(line)

prompts = []
for i in range(len(promptList)):
    prompts.append(promptList[i][(len(str(i+1))+2):])
            
def drawQuestion(canvas, data):
    canvas.create_text(data.width//2, data.height//4, text=data.prompts[data.index],font="Arial 10")

def drawEvals(canvas, data):
    rarely = canvas.create_rectangle(data.margin,data.height*0.7,data.margin+data.boxWidth,data.height*0.8,fill="red")
    sometimes = canvas.create_rectangle(data.margin+data.boxWidth,data.height*0.7,data.margin+2*data.boxWidth,data.height*0.8,fill="yellow")
    often = canvas.create_rectangle(data.margin,data.height*0.8,data.margin+data.boxWidth,data.height*0.9,fill="green")
    always = canvas.create_rectangle(data.margin+data.boxWidth,data.height*0.8,data.margin+2*data.boxWidth,data.height*0.9,fill="blue")
    
    rarelyText = canvas.create_text(data.margin+data.boxWidth/2, data.height*0.75,text="Rarely")
    sometimesText = canvas.create_text(data.margin+1.5*data.boxWidth, data.height*0.75,text="Sometimes")
    oftenText = canvas.create_text(data.margin+data.boxWidth/2, data.height*0.85,text="Often")
    alwaysText = canvas.create_text(data.margin+1.5*data.boxWidth, data.height*0.85,text="Always")

def getPrimaryStyle(data):
    primary = []
    primaryStyle = []
    maxScore = 0
    
    for style in data.styleValues:
        if style > maxScore:
            maxScore = style
            primary = [maxScore]
        elif style == maxScore:
            primary.append(style)
    
    if len(primary) == 1:
        primaryStyle = [data.styles.get(primary[0])]
    else:
        for prime in primary:
            primaryStyle.append(data.styles.get(prime))
    
    return primaryStyle

def getLeastStyle(data):
    least = []
    leastStyle = []
    minScore = 1000
    
    for style in data.styleValues:
        if style < minScore:
            minScore = style
            least = [minScore]
        elif style == minScore:
            least.append(style)
    
    if len(least) == 1:
        leastStyle = [data.styles.get(least[0])]
    else:
        for lease in least:
            leastStyle.append(data.styles.get(lease))
    
    return leastStyle

def drawTexts(canvas, data, s, v, height):
    canvas.create_text(data.width/2, data.height*height, text=str(s) + ": " + str(v))

def drawEnding(canvas, data):
    primaryStyle = getPrimaryStyle(data)
    leastStyle = getLeastStyle(data)
    mainResult = "Your primary style of conflict resolution is: "
    mainResult1 = "Your least likely style is: " 
    subResult = "Here's a breakdown of your results!"
    styles = ""
    
    if len(primaryStyle) == 1:
        mainResult += str(primaryStyle[0])
    else:
        for style in primaryStyle:
            primestyles += str(primaryStyle[style])
        mainResult += primestyles
    
    if len(leastStyle) == 1:
        mainResult1 += str(leastStyle[0])
    else:
        for style in leastStyle:
            leasestyles += str(leastStyle[style])
        mainResult1 += leasestyles
    
    canvas.create_rectangle(0, 0, data.width, data.height,fill='beige', width=0)
    canvas.create_text(data.width/2, data.height/4, text=mainResult)
    canvas.create_text(data.width/2, data.height*0.28, text=mainResult1)
    canvas.create_text(data.width/2, data.height/3,text=subResult)
    
    for style in data.styles:
        textHeight = 0.32
        drawTexts(canvas, data, style, data.styles[style], textHeight)
        textHeight += 0.05

def init(data):
    data.prompts = prompts
    data.index = 0
    data.margin = 50
    data.boxWidth = 150
    data.collaborating = 0
    data.competing = 0
    data.compromising = 0
    data.avoiding = 0
    data.accommodating = 0
    data.styles = {"Competing": data.competing, "Collaborating": data.collaborating, "Compromising": data.compromising, "Avoiding": data.avoiding, "Accommodating": data.accommodating}
    data.styleValues = [data.competing, data.collaborating, data.compromising, data.avoiding, data.accommodating]
    data.quizOver = False

def mousePressed(event, data):
    if data.index < len(data.prompts)-1:
        if ((data.index == 1) or (data.index == 5) or (data.index == 7)):
            if ((data.margin <= event.x <= (data.margin+data.boxWidth)) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.collaborating += 1
            elif ((data.margin+data.boxWidth <= event.x <= (data.margin+2*data.boxWidth)) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.collaborating += 2
            elif ((data.margin <= event.x <= (data.margin+data.boxWidth)) and (data.height*0.8 <= event.y <= data.height*0.9)): 
                data.collaborating += 3
            elif ((data.margin+data.boxWidth <= event.x <= (data.margin+2*data.boxWidth)) and (data.height*0.8 <= event.y <= data.height*0.9)): 
                data.collaborating += 4
        elif ((data.index == 2) or (data.index == 8) or (data.index == 13)):
            if ((data.margin <= event.x <= (data.margin+data.boxWidth)) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.compromising += 1
            elif ((data.margin+data.boxWidth <= event.x <= (data.margin+2*data.boxWidth)) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.compromising += 2
            elif ((data.margin <= event.x <= (data.margin+data.boxWidth)) and (data.height*0.8 <= event.y <= data.height*0.9)): 
                data.compromising += 3
            elif ((data.margin+data.boxWidth <= event.x <= (data.margin+2*data.boxWidth)) and (data.height*0.8 <= event.y <= data.height*0.9)): 
                data.compromising += 4
        elif ((data.index == 3) or (data.index == 11) or (data.index == 14)):
            if ((data.margin <= event.x <= (data.margin+data.boxWidth)) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.accommodating += 1
            elif ((data.margin+data.boxWidth <= event.x <= (data.margin+2*data.boxWidth)) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.accommodating += 2
            elif ((data.margin <= event.x <= (data.margin+data.boxWidth)) and (data.height*0.8 <= event.y <= data.height*0.9)): 
                data.accommodating += 3
            elif ((data.margin+data.boxWidth <= event.x <= (data.margin+2*data.boxWidth)) and (data.height*0.8 <= event.y <= data.height*0.9)): 
                data.accommodating += 4
        elif ((data.index == 4) or (data.index == 9) or (data.index == 12)):
            if ((data.margin <= event.x <= (data.margin+data.boxWidth)) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.competing += 1
            elif ((data.margin+data.boxWidth <= event.x <= (data.margin+2*data.boxWidth)) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.competing += 2
            elif ((data.margin <= event.x <= (data.margin+data.boxWidth)) and (data.height*0.8 <= event.y <= data.height*0.9)): 
                data.competing += 3
            elif ((data.margin+data.boxWidth <= event.x <= (data.margin+2*data.boxWidth)) and (data.height*0.8 <= event.y <= data.height*0.9)): 
                data.competing += 4
        elif ((data.index == 6) or (data.index == 10) or (data.index == 15)):
            if ((data.margin <= event.x <= (data.margin+data.boxWidth)) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.avoiding += 1
            elif ((data.margin+data.boxWidth <= event.x <= (data.margin+2*data.boxWidth)) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.avoiding += 2
            elif ((data.margin <= event.x <= (data.margin+data.boxWidth)) and (data.height*0.8 <= event.y <= data.height*0.9)): 
                data.avoiding += 3
            elif ((data.margin+data.boxWidth <= event.x <= (data.margin+2*data.boxWidth)) and (data.height*0.8 <= event.y <= data.height*0.9)): 
                data.avoiding += 4
            
        data.index += 1
    
    else:
        data.quizOver = not data.quizOver
        data.styles = {"Competing": data.competing, "Collaborating": data.collaborating, "Compromising": data.compromising, "Avoiding":
                        data.avoiding, "Accommodating": data.accommodating}
        data.styleValues = [data.competing, data.collaborating, data.compromising, data.avoiding, data.accommodating]
        
        print(data.styles)
    

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawQuestion(canvas, data)
    drawEvals(canvas, data)
    
    if data.quizOver:
        drawEnding(canvas, data)


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
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

run(400,400)