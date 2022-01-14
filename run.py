""" Import packages"""
import random

""" Import other task scripts """
from functions import *

""" Shuffle trial order """

trialTypes = list(range(16))
# random.shuffle(trialTypes)

random.shuffle(barColors)

""" Run trials """

for i in trialTypes:
    targetColors = barColors.copy()

    thisItemConstel = itemConstels[i]
    thisTargetLoc = targetLocs[i]

    targetCol, targetOri = trialSpecs(thisItemConstel, thisTargetLoc, targetColors, loadType=4)
    presentStim()
    clockwise, count = presentResponse(targetCol)
    presentTrialFeedback(clockwise, count, targetOri)

