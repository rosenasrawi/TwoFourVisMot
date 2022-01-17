""" Import packages"""

""" Import other task scripts """
from functions import *

""" Prepare block """
loadType = 2
trialTypes, targetColors = blockSpecs()
presentPrecueLoad(loadType, targetColors)

""" Run trials """

for i in trialTypes:
    # targetColors = barColors.copy()

    thisItemConstel = itemConstels[i]
    thisTargetLoc = targetLocs[i]

    targetCol, targetOri = trialSpecs(thisItemConstel, thisTargetLoc, targetColors, loadType)
    presentStim()
    clockwise, count = presentResponse(targetCol)
    presentTrialFeedback(clockwise, count, targetOri)

