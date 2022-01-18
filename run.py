""" Import other task scripts """

from functions import *

""" Prepare task """

random.shuffle(conditionOrder)

""" Prepare block """

for block in conditionOrder:
    thisBlockNum += 1
    presentBlockStart(thisBlockNum, numBlocks)

    loadType = loadTypes[block]; dialType = dialTypes[block]
    trialTypes, targetColors = blockSpecs()
    presentPrecueDial(dialType)
    presentPrecueLoad(loadType, targetColors)

    """ Run trials """

    performanceTrials = []

    for trial in trialTypes:
        thisItemConstel = itemConstels[trial]
        thisTargetLoc = targetLocs[trial]

        targetCol, targetOri = trialSpecs(thisItemConstel, thisTargetLoc, targetColors, loadType)
        presentStim()
        clockwise, count = presentResponse(targetCol, dialType)
        performance = presentTrialFeedback(clockwise, count, targetOri, dialType)

        performanceTrials.append(performance)

    presentBlockFeedback(performanceTrials)

presentTaskEnd()
