""" Import packages"""

""" Import other task scripts """
from functions import *

""" Prepare block """
loadType = 4; dialType = 'R'
trialTypes, targetColors = blockSpecs()
presentPrecueDial(dialType)
presentPrecueLoad(loadType, targetColors)

""" Run trials """

for i in trialTypes:
    thisItemConstel = itemConstels[i]
    thisTargetLoc = targetLocs[i]

    targetCol, targetOri = trialSpecs(thisItemConstel, thisTargetLoc, targetColors, loadType)
    presentStim()
    clockwise, count = presentResponse(targetCol, dialType)
    presentTrialFeedback(clockwise, count, targetOri, dialType)

