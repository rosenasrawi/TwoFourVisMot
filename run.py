""" Import other task scripts """

from logfile import *
filename, header = newLogfile()
from functions import *

""" Prepare task """

random.shuffle(conditionOrder)

""" Prepare block """

for block in conditionOrder:
    # Blockspecs
    loadType, dialType, trialTypes, targetColors, thisBlockNum = blockSpecs(block, thisBlockNum)

    # Start block
    presentBlockStart(thisBlockNum, numBlocks)
    presentPrecueDial(dialType)
    presentPrecueLoad(loadType, targetColors)

    """ Run trials """

    performanceTrials = []

    for trialType in trialTypes:
        # Trial specs
        thisItemConstel = itemConstels[trialType]; thisTargetLoc = targetLocs[trialType]
        targetCol, targetOri = trialSpecs(thisItemConstel, thisTargetLoc, targetColors, loadType)
        
        # Start trial
        thisFixTime = presentStim()
        clockwise, count, probeTime, pressTime, releaseTime = presentResponse(targetCol, dialType, False)
        reportOri, difference, performance = presentTrialFeedback(clockwise, count, targetOri, dialType)
        performanceTrials.append(performance)

        # Log trial data
        trialData = createTrialData(leftBarTop, rightBarTop, leftBarBot, rightBarBot, targetColors, 
                                    thisTargetLoc, targetOri, reportOri, count, clockwise, difference,
                                    performance, thisFixTime, probeTime, pressTime, releaseTime,
                                    dialType, loadType, trialType)
        addTrialLogfile(filename, header, trialData)

    presentBlockFeedback(performanceTrials)

presentTaskEnd()
