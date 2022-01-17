""" Import packages"""

""" Import other task scripts """
from functions import *

""" Prepare block """
loadType = 4
trialTypes, targetColors = blockSpecs()

""" Run trials """

for i in trialTypes:
    # targetColors = barColors.copy()

    thisItemConstel = itemConstels[i]
    thisTargetLoc = targetLocs[i]

    targetCol, targetOri = trialSpecs(thisItemConstel, thisTargetLoc, targetColors, loadType)
    presentStim()
    clockwise, count = presentResponse(targetCol)
    presentTrialFeedback(clockwise, count, targetOri)

