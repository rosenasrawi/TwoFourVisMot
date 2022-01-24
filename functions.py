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

def taskSpecs():

    dialTypes = []; loadTypes = []
    
    D = ['U','R']; L = [2,4]
    random.shuffle(D)

    for d in range(len(D)):
        dialTypes += [D[d]]*len(L)
        random.shuffle(L)
        loadTypes += L

    trialTypes = list(range(16))

    numBlocks = len(dialTypes); 
    thisBlockNum = 0

    return dialTypes, loadTypes, trialTypes, numBlocks, thisBlockNum

""" Block specifics """

def blockSpecs(block, thisBlockNum, loadTypes, dialTypes, trialTypes):

    thisBlockNum += 1
    loadType = loadTypes[block]; dialType = dialTypes[block]

    targetColors = barColors.copy()
    random.shuffle(targetColors)
    random.shuffle(trialTypes)
    
    return loadType, dialType, trialTypes, targetColors, thisBlockNum

""" Precue: dialtype"""

def presentPrecueDial(dialType):
    oris = ['L','R','L','R','L','R']
    random.shuffle(oris)
    precueTextDial.setAutoDraw(True)
    precueTextDialButtons.setAutoDraw(True)

    for i in oris:
        if i == 'L': ori = random.randint(oriRangeLeft[0], oriRangeLeft[1])
        elif i == 'R': ori = random.randint(oriRangeRight[0], oriRangeRight[1])
        practiceBar.ori = ori
        practiceBar.fillColor = random.choice(barColors)

        practiceBar.setAutoDraw(True)
        clockwise, count, probeTime, pressTime, releaseTime = presentResponse(fixColor, dialType, True)
        practiceBar.setAutoDraw(False)
        presentTrialFeedback(clockwise,count,practiceBar.ori, dialType)
    
    precueTextDial.setAutoDraw(False)
    precueTextDialButtons.setAutoDraw(False)

""" Precue: loadtype"""

def presentPrecueLoad(loadType, targetColors):

    if loadType == 4:
        # Set specs
        precueColors4a.color = targetColors[0]
        precueColors4a.text = barColorNames[barColors.index(targetColors[0])]
        
        precueColors4b.color = targetColors[1]
        precueColors4b.text = barColorNames[barColors.index(targetColors[1])]
        
        precueColors4c.color = targetColors[2]
        precueColors4c.text = barColorNames[barColors.index(targetColors[2])]
        
        precueColors4d.color = targetColors[3]
        precueColors4d.text = barColorNames[barColors.index(targetColors[3])]

        # Turn objects on
        precueColors4a.draw()
        precueColors4b.draw()
        precueColors4c.draw()
        precueColors4d.draw()

    elif loadType == 2:
        # Set specs
        precueColors2a.color = targetColors[0]
        precueColors2a.text = barColorNames[barColors.index(targetColors[0])]
        
        precueColors2b.color = targetColors[1]
        precueColors2b.text = barColorNames[barColors.index(targetColors[1])]

        # Turn objects on
        precueColors2a.draw()
        precueColors2b.draw()

    precueTextColor.draw()
    fixCross.draw()
    space2continue.draw()

    mywin.flip()
    event.waitKeys(keyList = 'space')

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
        leftBarTop.fillColor = targetColors[0]; rightBarTop.fillColor = targetColors[1]
        leftBarBot.fillColor = targetColors[2]; rightBarBot.fillColor = targetColors[3]
    elif loadType == 2:     # Load two
        distrib = colorDistrib[thisTargetLoc]
        t = random.randint(0,1)
        bars[distrib[0]].fillColor = targetColors[t]
        bars[distrib[1]].fillColor = targetColors[1-t]
        bars[distrib[2]].fillColor = targetColors[2]
        bars[distrib[3]].fillColor = targetColors[3]

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
    
    for i in range(thisFixTime):              # Fixation
        mywin.flip()
    
    leftBarTop.setAutoDraw(True)
    rightBarTop.setAutoDraw(True)
    leftBarBot.setAutoDraw(True)
    rightBarBot.setAutoDraw(True)

    for i in range(encodingTime):             # Encoding display
        mywin.flip()

    leftBarTop.setAutoDraw(False)
    rightBarTop.setAutoDraw(False)
    leftBarBot.setAutoDraw(False)
    rightBarBot.setAutoDraw(False)

    for i in range(delayTime):                # Memory delay
        mywin.flip()

    return thisFixTime

""" Present response dial """

def presentResponse(targetCol, dialType, practice):

    # Reset
    kb.clearEvents()

    count = 0 # positions not updated yet
    clockwise = False
    key_release = []
    key_press = []

    # Trial settings
    fixCross.lineColor = targetCol
    if dialType == 'U':
        turnUpper.pos = upper_turnUpper             # Dial circles in the upper positions
        turnLower.pos = upper_turnLower
    elif dialType == 'R':
        turnUpper.pos = right_turnUpper             # Dial circles in the upper positions
        turnLower.pos = right_turnLower

    # Response objects on
    if not practice: fixCross.setAutoDraw(True)
    if practice:
        responseCircle.setAutoDraw(True) 
        turnLower.setAutoDraw(True) 
        turnUpper.setAutoDraw(True) 
    probeTime = time.time()

    mywin.flip()

    key_press = event.waitKeys(keyList = ['z', 'm', 'q', 'escape'])     # Wait for a keypress
    pressTime = time.time()
    if not practice:
        responseCircle.setAutoDraw(True) 
        turnLower.setAutoDraw(True) 
        turnUpper.setAutoDraw(True) 

    if 'z' in key_press:
        clockwise = False; key = 'z'; thisTurn = -radStep
    elif 'm' in key_press:
        clockwise = True; key = 'm'; thisTurn = radStep
    elif 'q' in key_press:
        core.quit()

    while key_release == [] and count < maxTurn:
        
        key_release = kb.getKeys(keyList = [key], waitRelease = True, clear = True)

        positions = turnPositionsCircle(turnUpper.pos, turnLower.pos, thisTurn = thisTurn)
        turnUpper.pos = positions[0]
        turnLower.pos = positions[1]

        count += 1 # one step updated

        mywin.flip()
    
    releaseTime = time.time()
    key_press = []
    key_release = []

    # Response objects off
    responseCircle.setAutoDraw(False) 
    turnLower.setAutoDraw(False) 
    turnUpper.setAutoDraw(False)
    fixCross.setAutoDraw(False)

    return clockwise, count, probeTime, pressTime, releaseTime

""" Trial feedback """

def presentTrialFeedback(clockwise, count, targetOri, dialType):

    # Determine response orientation
    if clockwise == False: # Z press
        reportOri = degrees(count * radStep)*-1
    if clockwise == True: # M press
        reportOri = degrees(count * radStep)    

    if dialType == 'R':
        reportOri += 90
        if targetOri < 0: targetOri += 180

    difference = abs(targetOri - round(reportOri))

    if difference > 90: # difference can't be more than 90
        difference -= 180
        difference *= -1

    performance = round(100 - difference/90 * 100)
    feedbackText.text = str(performance)

    fixCross.setAutoDraw(True)
    feedbackText.setAutoDraw(True)

    for i in range(feedbackTime): # 250 ms 
        mywin.flip()

    fixCross.setAutoDraw(False)
    feedbackText.setAutoDraw(False)   

    return reportOri, difference, performance

""" Eye calibration screen """

def myTrackCalibration():

    # Please follow the dot in 3, 2, 1:
    eyecalibrationText.setAutoDraw(True)
    eyecalibrationCounterText.setAutoDraw(True)

    counterText = ['3', '', '2', '', '1', '']
    for cT in counterText:
        eyecalibrationCounterText.text = cT
        for i in range(counterTime): # 500 ms
            mywin.flip()

    eyecalibrationText.setAutoDraw(False)
    eyecalibrationCounterText.setAutoDraw(False)

    # Dots start to appear
    eyecalibrationCircle.setAutoDraw(True)
    eyecalibrationCircleMini.setAutoDraw(True)

    posOrder = list(range(len(allPositions)))
    random.shuffle(posOrder)

    for pos in posOrder:
        eyecalibrationCircle.pos = list(allPositions[pos])
        eyecalibrationCircleMini.pos = list(allPositions[pos])

        for i in range(calibrationTime): # 1500 ms
            mywin.flip()

    eyecalibrationCircle.setAutoDraw(False)
    eyecalibrationCircleMini.setAutoDraw(False)   
               
""" Block feedback """

def presentBlockFeedback(performanceTrials):

    performanceBlock = round(mean(performanceTrials))
    blockFeedbackPerformanceText.text = str(performanceBlock) + "% correct"

    blockFeedbackText.draw()
    blockFeedbackPerformanceText.draw()
    space2continue.draw()

    mywin.flip()
    event.waitKeys(keyList = 'space')        
  
""" Block start """

def presentBlockStart(thisBlockNum, numBlocks):

    blockStartText.text = "Press [space] to start block " + str(thisBlockNum) + "/" + str(numBlocks)
    blockStartText.draw()
    mywin.flip()
    event.waitKeys(keyList = 'space')       

""" Task end """

def presentTaskEnd():
    
    taskEndText.draw()
    mywin.flip()
    event.waitKeys(keyList = 'space')    
