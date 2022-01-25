""" Input on what task to run """

taskInput = input('Do you wish to run the main task (Y/N)? ')
if taskInput == 'Y' or taskInput == 'y': isTask = True
elif taskInput == 'N' or taskInput == 'n': isTask = False
else: print('Error: incorrect input value (not Y or N), please try running the script again.')

""" Import other task scripts """

if isTask:
    from logfile import *
    filename, header = newLogfile()
from functions import *

""" Prepare task """

dialTypes, loadTypes, trialTypes, numBlocks, thisBlockNum = taskSpecs(isTask)

""" Prepare block """

for block in range(len(dialTypes)):
    # Blockspecs
    loadType, dialType, trialTypes, targetColors, thisBlockNum = blockSpecs(block, thisBlockNum, loadTypes, dialTypes, trialTypes)

    # Start block
    presentBlockStart(thisBlockNum, numBlocks)

    # Pre-cues
    if block == 0 or block != 0 and dialType != dialTypes[block-1]:
        presentPrecueDial(dialType)
    presentPrecueLoad(loadType, targetColors)

    """ Run trials """

    performanceTrials = []

    for trialType in trialTypes:
        if isTask: 
            encTrig, probeTrig, respTrig = trialTriggers(trialType, loadType, dialType)

        # Trial specs
        thisItemConstel = itemConstels[trialType]; thisTargetLoc = targetLocs[trialType]
        targetCol, targetOri = trialSpecs(thisItemConstel, thisTargetLoc, targetColors, loadType)
        
        # Start trial
        thisFixTime = presentStim(isTask, encTrig)
        clockwise, count, probeTime, pressTime, releaseTime = presentResponse(targetCol, dialType, False, isTask, probeTrig, respTrig)
        reportOri, difference, performance = presentTrialFeedback(clockwise, count, targetOri, dialType)
        performanceTrials.append(performance)

        # Log trial data
        if isTask:
            trialData = createTrialData(leftBarTop, rightBarTop, leftBarBot, rightBarBot, targetColors, 
                                        thisTargetLoc, targetOri, reportOri, count, clockwise, difference,
                                        performance, thisFixTime, probeTime, pressTime, releaseTime,
                                        dialType, loadType, trialType, thisBlockNum, encTrig, probeTrig, respTrig)
            addTrialLogfile(filename, header, trialData)

    presentBlockFeedback(performanceTrials)
    
    if block != len(dialTypes)-1:
        myTrackCalibration()

presentTaskEnd()
