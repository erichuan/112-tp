'''
General animation framework taken from 112 course notes
'''
from tkinter import *
import random


prompt1 = "I enjoy digging into the issues to find solutions that work for everybody"
prompt2 = "I do my best to negotiate a “give-and-take” approach to conflict"
prompt3 = "I believe it’s important to keep relationships civil \nand associates happy"
prompt4 = "It’s important to argue my case well to convince the other \nperson of the merits of my position"
prompt5 = "In times of conflict, I gather as many facts as I can to \nkeep the conversation productive"
prompt6 = "In a conflict situation, I am calm and collected and usually \nleave as soon as possible"
prompt7 = "I approach conflict from both sides of the argument. \nWhat are my needs? What will work for the other person? \nWhat are the actual issues?"
prompt8 = "My preferred way of dealing with conflict is to compromise and \nmove past the discomfort"
prompt9 = "Often, I enjoy conflict. It is challenging and allows me to \nengage my intellect"
prompt10 = "Conflict makes me feel stressed and anxious"
prompt11 = "When I see an obvious solution, I argue my case strongly"
prompt12 = "If it comes to a stand off, I will meet people halfway"
prompt13 = "Keeping the peace is my priority. I don’t like tension"
prompt14 = "When I have bad feelings about someone, I keep them to myself"

prompts = [prompt1, prompt2, prompt3, prompt4, prompt5, prompt6, prompt7, prompt8, prompt9, prompt10, prompt11, prompt12, prompt13, prompt14]

competingText = '''
As someone with competing as the primary style of conflict resolution, you 
typically value your goals over relationships, meaning that if forced to choose, 
you tend to seek your goals even at the cost of the relationship involved.
'''

collaboratingText = '''
As someone with collaborating as the primary style of conflict resolution, you value 
both your goals and relationships equally as important. You tend to view conflict 
as problems to be solved and seek solutions that achieves the goals of those 
involved. You'll work to reduce tensions between the conflicting parties through
starting open dialogue that helps keep tensions low.
'''

compromisingText = '''
As someone with compromising as the primary style of conflict resolution, you are
moderately concerned with both the goals and relationships with others. As a compromise, 
you tend to give up part of your goals and persuade others to give up part of 
their goals as well. You tend to seek a solution in which both sides give-take. 
You are willing to sacrifice part of their goals in order to find agreement for 
the common good.
'''

avoidingText = '''
As someone with avoiding as the primary style of conflict, you tend to be more
confrontation-averse. You may find it easier to withdraw from a conflict than 
to face it. Sometimes, this might even include completely giving up relationships 
or goals that are associated with the conflict. 
'''

accommodatingText = '''
As someone with accommodating as the primary style of conflict, you value your
relationships over your own goals. You generally want to be liked by others, and 
prefer to be conflict-averse if you see the conflict likely of damaging relationships. 
'''

citation = '''
Assessment adapted from 
http://www.blake-group.com/sites/default/files/assessments/Conflict_Management_Styles_Assessment.pdf,
which is based on “Conflict and Negotiation Processes in Organizations” 
by K. Thomas in M. D. Dunnette and L. M. Hough (eds.), Handbook of Industrial 
and Organizational Psychology, 2/e, vol. 3 (Palo Alto, CA: Consulting 
Psychologists Press, 1992), 668.
'''
            
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
    maxScore = max(data.styleValues)
    
    for key in data.styles:
        if data.styles[key] == maxScore:
            primary.append(key)
    
    return primary

def getLeastStyle(data):
    least = []
    minScore = min(data.styleValues)
    
    for key in data.styles:
        if data.styles[key] == minScore:
            least.append(key)
    
    return least

def drawTexts(canvas, data):
    height = 0.35
    for style in data.styles:
        canvas.create_text(data.width/2, data.height*height, text=str(style) + ": " + " "*5 + str(data.styles[style]),font="Arial 14", anchor="e")
        height += 0.05
    

def drawEnding(canvas, data):
    primaryStyle = getPrimaryStyle(data)
    leastStyle = getLeastStyle(data)
    mainResult = "Your primary style of conflict resolution is: "
    mainResult1 = ""
    mainResult2 = "Your least likely style is: " 
    mainResult3 = ""
    subResult = "Here's a breakdown of your results!"
    primestyles = ""
    leasestyles = ""
    analys = ''''''
    styleAnalysis = ''''''
    data.citation = citation
    
    if len(primaryStyle) == 1:
        mainResult1 = str(primaryStyle[0])
        styleAnalysis = data.styleAnalyses[primaryStyle[0]]
    else:
        for style in primaryStyle:
            primestyles += str(style)
            primestyles += ", "
            analys += data.styleAnalyses[style]
            analys += "\n"
        mainResult1 += primestyles[:-2]
        styleAnalysis += analys[:-1]
    
    if len(leastStyle) == 1:
        mainResult3 = str(leastStyle[0])
    else:
        for style in leastStyle:
            leasestyles += str(style)
            leasestyles += ", "
        mainResult3 += leasestyles[:-2]
    
    canvas.create_rectangle(0, 0, data.width, data.height,fill='beige', width=0)
    canvas.create_text(data.width/2, data.height*0.12, text=mainResult, font="Arial 14")
    canvas.create_text(data.width/2, data.height*0.15, text=mainResult1, font="Arial 14")
    canvas.create_text(data.width/2, data.height*0.22, text=mainResult2, font="Arial 14")
    canvas.create_text(data.width/2, data.height/4, text=mainResult3, font="Arial 14")
    canvas.create_text(data.width/2, data.height*0.3, text=subResult, font="Arial 14")
    drawTexts(canvas, data)
    canvas.create_text(data.width/2, data.height*0.72, text=styleAnalysis, font="Arial 10")
    canvas.create_text(data.width*0.75, data.height*0.92, text="Press 'a' to try again", font="Arial 10")
    canvas.create_text(data.width*0.75, data.height*0.95, text="Press 'r' for references", font="Arial 10")

def init(data):
    data.prompts = prompts
    data.index = 0
    data.margin = data.width//6
    data.boxWidth = data.width*0.325
    data.collaborating = 0
    data.competing = 0
    data.compromising = 0
    data.avoiding = 0
    data.accommodating = 0
    data.styles = {"Competing": data.competing, "Collaborating": data.collaborating, "Compromising": data.compromising, "Avoiding": data.avoiding, "Accommodating": data.accommodating}
    data.styleValues = [data.competing, data.collaborating, data.compromising, data.avoiding, data.accommodating]
    data.quizOver = False
    data.caption = False
    data.styleAnalyses = {"Competing": competingText, "Collaborating": collaboratingText, "Compromising": compromisingText, "Avoiding": avoidingText, "Accommodating": accommodatingText}

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
        data.quizOver = True
        data.styles = {"Competing": data.competing, "Collaborating": data.collaborating, "Compromising": data.compromising, "Avoiding":
                        data.avoiding, "Accommodating": data.accommodating}
        data.styleValues = [data.competing, data.collaborating, data.compromising, data.avoiding, data.accommodating]
            
def keyPressed(event, data):
    if event.keysym == "r":
        data.caption = True
    elif event.keysym == "space":
        data.caption = False
    elif event.keysym == "a":
        init(data)

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawQuestion(canvas, data)
    drawEvals(canvas, data)
    
    if data.quizOver:
        drawEnding(canvas, data)
        if data.caption:
            canvas.create_rectangle(data.width/2-200,data.height/2-75,data.width/2+200,data.height/2+75,fill="red")
            canvas.create_text(data.width/2, data.height/2, text=data.citation, fill="white", font="Arial 8")
        else:
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

run(600,400)