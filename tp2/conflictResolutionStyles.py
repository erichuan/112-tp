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


class ResolutionType(object):
    def __init__(self, resolutionStyle):
        self.resolutionStyle = resolutionStyle
        self.assertive = ("assertiveness", None)
        self.competitive = ("competitiveness", None)
        self.resolution = (self.resolutionStyle, self.assertive, self.competitive)
    
    def assertiveness(self):
        if self.resolutionStyle == "Competing":
            self.level = "high"
            self.assertive[1] = self.level
        elif self.resolutionStyle == "Collaborating":
            self.level = "high"
            self.assertive[1] = self.level
        elif self.resolutionStyle == "Compromising":
            self.level = "medium"
            self.assertive[1] = self.level
        elif self.resolutionStyle == "Avoiding":
            self.level = "low"
            self.assertive[1] = self.level
        elif self.resolutionStyle == "Accommodating":
            self.level = "low"
            self.assertive[1] = self.level
    
    def competitiveness(self):
        if self.resolutionStyle == "Competing":
            self.level = "low"
            self.competitive[1] = self.level
        elif self.resolutionStyle == "Collaborating":
            self.level = "high"
            self.competitive[1] = self.level
        elif self.resolutionStyle == "Compromising":
            self.level = "medium"
            self.competitive[1] = self.level
        elif self.resolutionStyle == "Avoiding":
            self.level = "low"
            self.competitive[1] = self.level
        elif self.resolutionStyle == "Accommodating":
            self.level = "high"
            self.competitive[1] = self.level
            
def drawQuestion(canvas, data):
    canvas.create_text(data.width//2, data.height//4, text=data.prompts[data.index],font="Arial 10")

def drawEvals(canvas, data):
    rarely = canvas.create_text(data.margin, data.height*0.75,text="Rarely", anchor="nw")
    sometimes = canvas.create_text(data.margin+data.partition, data.height*0.75,text="Sometimes", anchor="n")
    often = canvas.create_text(data.margin+data.partition*2, data.height*0.75,text="Often", anchor="n")
    always = canvas.create_text(data.width-data.margin, data.height*0.75,text="Always", anchor="ne")

def drawEnding(canvas, data):
    canvas.create_text(data.width//2, data.height//4, text="Quiz Over")
        
def init(data):
    data.style = "" # ["Competing", "Collaborating", "Compromising", "Avoiding", "Accommodating"]
    data.resolutionType = ResolutionType(data.style)
    data.prompts = prompts
    data.index = 0
    data.margin = 15
    data.lineLength = data.width-2*data.margin
    data.partition = data.lineLength/3
    data.collaborating = 0
    data.competing = 0
    data.compromising = 0
    data.avoiding = 0
    data.accommodating = 0
    data.quizOver = False

def mousePressed(event, data):
    if data.index < len(data.prompts):
        if ((data.index == 1) or (data.index == 5) or (data.index == 7)):
            if ((0 <= event.x <= data.margin) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.collaborating += 1
            elif ((data.margin <= event.x <= data.margin+data.partition) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.collaborating += 2
            elif ((data.margin+data.partition <= event.x <= data.margin+2*data.partition) and 
                  (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.collaborating += 3
            elif ((data.margin+data.partition*2 <= event.x <= data.width-data.margin) and 
                  (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.collaborating += 4
        elif ((data.index == 2) or (data.index == 8) or (data.index == 13)):
            if ((0 <= event.x <= data.margin) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.compromising += 1
            elif ((data.margin <= event.x <= data.margin+data.partition) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.compromising += 2
            elif ((data.margin+data.partition <= event.x <= data.margin+2*data.partition) and 
                  (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.compromising += 3
            elif ((data.margin+data.partition*2 <= event.x <= data.width-data.margin) and 
                  (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.compromising += 4
        elif ((data.index == 3) or (data.index == 11) or (data.index == 14)):
            if ((0 <= event.x <= data.margin) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.accommodating += 1
            elif ((data.margin <= event.x <= data.margin+data.partition) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.accommodating += 2
            elif ((data.margin+data.partition <= event.x <= data.margin+2*data.partition) and 
                  (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.accommodating += 3
            elif ((data.margin+data.partition*2 <= event.x <= data.width-data.margin) and 
                  (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.accommodating += 4
        elif ((data.index == 4) or (data.index == 9) or (data.index == 12)):
            if ((0 <= event.x <= data.margin) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.competing += 1
            elif ((data.margin <= event.x <= data.margin+data.partition) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.competing += 2
            elif ((data.margin+data.partition <= event.x <= data.margin+2*data.partition) and 
                  (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.competing += 3
            elif ((data.margin+data.partition*2 <= event.x <= data.width-data.margin) and 
                  (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.competing += 4
        elif ((data.index == 6) or (data.index == 10) or (data.index == 15)):
            if ((0 <= event.x <= data.margin) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.avoiding += 1
            elif ((data.margin <= event.x <= data.margin+data.partition) and (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.avoiding += 2
            elif ((data.margin+data.partition <= event.x <= data.margin+2*data.partition) and 
                  (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.avoiding += 3
            elif ((data.margin+data.partition*2 <= event.x <= data.width-data.margin) and 
                  (data.height*0.7 <= event.y <= data.height*0.8)): 
                data.avoiding += 4
            
        data.index += 1
    
    print("collaborating= ", data.collaborating, "compromising= ", data.compromising, "competing= ", data.competing,
          "accommodating= ", data.accommodating, "avoiding= ", data.avoiding)
    if data.index > len(data.prompts):
        data.quizOver = not data.quizOver
    

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