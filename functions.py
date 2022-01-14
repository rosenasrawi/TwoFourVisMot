""" Import packages"""

from psychopy import core, event
from math import degrees, cos, sin
from statistics import mean
import random, time

""" Import other task scripts """

from objects import *                              # Task objects

""" Turning the dial """

def turnPositionsCircle(turnUpperPos, turnLowerPos, thisTurn):

    turnUpperPos = [turnUpperPos[0] * cos(thisTurn) + turnUpperPos[1] * sin(thisTurn),
                    -turnUpperPos[0] * sin(thisTurn) + turnUpperPos[1] * cos(thisTurn)]
    turnLowerPos = [turnLowerPos[0] * cos(thisTurn) + turnLowerPos[1] * sin(thisTurn),
                    -turnLowerPos[0] * sin(thisTurn) + turnLowerPos[1] * cos(thisTurn)]
    
    return turnUpperPos, turnLowerPos

""" Block specifics """

def blockSpecs():
    targetColors = barColors.copy(); #random.shuffle(targetColors)

    return targetColors

""" Trial specifics """

def trialSpecs(thisItemConstel, thisTargetLoc, targetColors, loadType):
    bars = [leftBarTop, rightBarTop, leftBarBot, rightBarBot]
    
    # Bar orientations
    constel = constelTypes[thisItemConstel]; oris = []
    for i in constel:
        if i == 'L': ori = random.randint(oriRangeLeft[0], oriRangeLeft[1])
        elif i == 'R': ori = random.randint(oriRangeRight[0], oriRangeRight[1])
        oris.append(ori)

    leftBarTop.ori = oris[0]; rightBarTop.ori = oris[1]
    leftBarBot.ori = oris[2]; rightBarBot.ori = oris[3]

    # Bar colors
    if loadType == 4:       # Load four
        random.shuffle(targetColors) 
        leftBarTop.fillColor = targetColors.pop(); rightBarTop.fillColor = targetColors.pop()
        leftBarBot.fillColor = targetColors.pop(); rightBarBot.fillColor = targetColors.pop()
    elif loadType == 2:     # Load two
        

        targetCol = targetColors.pop(random.randint(0,1)); nonTargetCol = targetColors.pop(0)

        distrib = colorDistrib[thisTargetLoc]

        bars[distrib[0]].fillColor = targetCol
        bars[distrib[1]].fillColor = nonTargetCol
        bars[distrib[2]].fillColor = targetColors.pop()
        bars[distrib[3]].fillColor = targetColors.pop()

    # Determine target bar
    targetBar = bars[thisTargetLoc-1]

    # Target ori & col
    targetCol = targetBar.fillColor; targetOri = targetBar.ori

    return targetCol, targetOri

""" Present main stimuli """

def presentStim():

    fixCross.lineColor = fixColor   
    fixCross.setAutoDraw(True)

    thisFixTime = random.randint(fixTime[0], fixTime[1])
    
    for i in range(thisFixTime):             # Fixation
        mywin.flip()
    
    leftBarTop.setAutoDraw(True)
    rightBarTop.setAutoDraw(True)
    leftBarBot.setAutoDraw(True)
    rightBarBot.setAutoDraw(True)

    for i in range(encodingTime):             # First encoding display
        mywin.flip()

    leftBarTop.setAutoDraw(False)
    rightBarTop.setAutoDraw(False)
    leftBarBot.setAutoDraw(False)
    rightBarBot.setAutoDraw(False)

    for i in range(delayTime):            # Memory delay
        mywin.flip()

    return thisFixTime

""" Present response dial """

def presentResponse(targetCol):

    # Reset
    kb.clearEvents()

    count = 0 # positions not updated yet
    clockwise = False
    key_release = []
    key_press = []

    # Trial settings
    fixCross.lineColor = targetCol
    turnUpper.pos = upper_turnUpper             # Dial circles in the correct position
    turnLower.pos = upper_turnLower

    # Response objects on
    fixCross.setAutoDraw(True)
    responseCircle.setAutoDraw(True) 
    turnLower.setAutoDraw(True) 
    turnUpper.setAutoDraw(True) 

    mywin.flip()

    key_press = event.waitKeys(keyList = ['z', 'm', 'q', 'escape'])     # Wait for a keypress

    if 'z' in key_press:
        clockwise = False

        while key_release == [] and count < maxTurn:
            
            key_release = kb.getKeys(keyList = ['z'], waitRelease = True, clear = True)

            positions = turnPositionsCircle(turnUpper.pos, turnLower.pos, thisTurn = -radStep)
            turnUpper.pos = positions[0]
            turnLower.pos = positions[1]

            count += 1 # one step updated

            mywin.flip()

    elif 'm' in key_press:
        clockwise = True

        while key_release == [] and count < maxTurn:

            key_release = kb.getKeys(keyList = ['m'], waitRelease = True, clear = True)

            positions = turnPositionsCircle(turnUpper.pos, turnLower.pos, thisTurn = radStep)
            turnUpper.pos = positions[0]
            turnLower.pos = positions[1]  

            count += 1 # one step updated
            mywin.flip()

    elif 'q' in key_press:
        core.quit()
        
    key_press = []
    key_release = []

    # Response objects off
    responseCircle.setAutoDraw(False) 
    turnLower.setAutoDraw(False) 
    turnUpper.setAutoDraw(False)
    fixCross.setAutoDraw(False)

    return clockwise, count

""" Trial feedback """

def presentTrialFeedback(clockwise, count, targetOri):

    # Determine response orientation
    if clockwise == False: # Z press
        reportOri = degrees(count * radStep)*-1
    if clockwise == True: # M press
        reportOri = degrees(count * radStep)    

    difference = abs(targetOri - round(reportOri))

    performance = round(100 - difference/90 * 100)
    feedbackText.text = str(performance)

    fixCross.setAutoDraw(True)
    feedbackText.setAutoDraw(True)

    for i in range(feedbackTime): # 250 ms 
        mywin.flip()

    fixCross.setAutoDraw(False)
    feedbackText.setAutoDraw(False)      
