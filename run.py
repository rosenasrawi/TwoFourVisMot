""" Input on what task to run """

taskInput = input('Do you wish to run the main task (y/n)? ')
if taskInput == 'Y' or taskInput == 'y': isTask = True
elif taskInput == 'N' or taskInput == 'n': isTask = False
else: print('Error: incorrect input value (not y or n), please try running the script again.')

""" Import other task scripts """

from logfile import *
filename, header, subjectID, session = newLogfile()

from functions import *

if isTask:
    from EEG_and_tracker import *  
    portEEG = connectEEG()
    tracker = connectTracker(subjectID, session)
    startTracker(tracker)
else: portEEG = []; tracker = []

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
        # if isTask: 
        encTrig, probeTrig, respTrig = trialTriggers(trialType, loadType, dialType)

        # Trial specs
        thisItemConstel = itemConstels[trialType]; thisTargetLoc = targetLocs[trialType]
        targetCol, targetOri = trialSpecs(thisItemConstel, thisTargetLoc, targetColors, loadType)
        
        # Start trial
        thisFixTime = presentStim(isTask, encTrig, portEEG, tracker)
        clockwise, count, probeTime, pressTime, releaseTime = presentResponse(targetCol, dialType, False, isTask, probeTrig, respTrig, portEEG, tracker)
        reportOri, difference, performance = presentTrialFeedback(clockwise, count, targetOri, dialType)
        performanceTrials.append(performance)

        # Log trial data
        trialData = createTrialData(leftBarTop, rightBarTop, leftBarBot, rightBarBot, targetCol, 
                                    thisTargetLoc, targetOri, reportOri, count, clockwise, difference,
                                    performance, thisFixTime, probeTime, pressTime, releaseTime,
                                    dialType, loadType, trialType, thisBlockNum, encTrig, probeTrig, respTrig)
        addTrialLogfile(filename, header, trialData)

    presentBlockFeedback(performanceTrials)
    
    if block != len(dialTypes)-1:
        myTrackCalibration(isTask, portEEG, tracker)
        if isTask:
            calibrateTracker(tracker)

if isTask:
    presentSavingData()
    stopTracker(tracker)

presentTaskEnd()
