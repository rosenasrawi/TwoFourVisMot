""" Import packages"""

from math import pi, atan2, degrees
import itertools

""" Configuration parameters """

# Computer settings
setting = 'home'
screen = 'laptop'
portType = 'parallel'

if setting == 'home':
    dataDirectory = '/Users/rosenasrawi/Documents/VU PhD/Projects/rn4:Mika - Vis-mot four items/Data/pilot/logfiles/'
    if screen == 'laptop':
        monitorHZ = 60
        monitorSize = [1536,960]
        height = 22; distance = 50; vertResolution = 1536 
    elif screen == 'monitor':
        monitorHZ = 60
        monitorSize = [2560,1440]
        height = 35; distance = 70; vertResolution = 2560 

elif setting == 'lab':
    eyeDirectory = 'hello'; dataDirectory = 'hello2'

    monitorHZ = 239
    monitorSize = [1920,1080]
    height = 28; distance = 60; vertResolution = 1920 

deg_per_px = degrees(atan2(.5*height, distance)) / (.5*vertResolution) # Calculate the number of degrees that correspond to a single pixel

# Sizes
barSize = [int(0.4/deg_per_px), int(3/deg_per_px)] # width, height 
fixSize = int(0.2/deg_per_px); LineWidth = int(0.05/deg_per_px)

circleRadius = int(1.5/deg_per_px)
miniCircleRadius = int(0.15/deg_per_px)
circleEdges = int(1/deg_per_px)

# Degrees and ranges
maxTurn = monitorHZ
quarterCircle = 0.5*pi
radStep = quarterCircle/maxTurn

oriRangeLeft = [-80, -10]
oriRangeRight = [10, 80]

# Locations
leftBarTopPos = [-int(3/deg_per_px), int(3/deg_per_px)]     # Left top
rightBarTopPos = [int(3/deg_per_px), int(3/deg_per_px)]     # Right top
leftBarBotPos = [-int(3/deg_per_px), -int(3/deg_per_px)]    # Left bottom
rightBarBotPos = [int(3/deg_per_px), -int(3/deg_per_px)]    # Right bottom

leftBarPos = [-int(3/deg_per_px), 0]
rightBarPos = [int(3/deg_per_px), 0] 

fixPos = [0,0]

upper_turnUpper = [0, circleRadius] # 
upper_turnLower = [0, -circleRadius]
right_turnUpper = [circleRadius, 0]
right_turnLower = [-circleRadius, 0]

# Colors
backgroundColor = (50/510, 50/510, 50/510)                  # darkdrey
barColors = ["#C2A025", "#3843C2", "#2FC259", "#CF3C3C"]
barColorNames = ['YELLOW', 'BLUE', 'GREEN', 'RED']       
fixColor = (300/510,300/510,300/510)                        # lightgrey
eyeCalibMini = (1/510, 1/510, 1/510)

# Timings
fixTime = [int(monitorHZ/2), int(monitorHZ*8/10)]   # 500, 800 ms
encodingTime = int(monitorHZ/4)                     # 250 ms
delayTime = int(monitorHZ*2.25)                     # 2250 ms
feedbackTime = int(monitorHZ/4)                     # 250 ms
counterTime = int(monitorHZ/2)                      # 500 ms
calibrationTime = int(monitorHZ)

# Text
textFont = 'Helvetica'
fontSizeFeedback = int(0.3/deg_per_px)
fontSizePreCue = int(0.4/deg_per_px)
fontColor = fixColor                                # lightgrey

# Trial types
itemConstels     = [1,1,1,1, 2,2,2,2, 3,3,3,3, 4,4,4,4]
targetLocs       = [1,2,3,4, 1,2,3,4, 1,2,3,4, 1,2,3,4]

# Orientation of items, based on consteltype (1-4)
constelTypes = {1: ['R','L','R','L'], 2: ['L','L','R','R'], 3: ['L','R','L','R'], 4: ['R','R','L','L']}

# Color distribution load two, based on targetlocation (1-4)
colorDistrib = {1: [0,3,1,2], 2: [1,2,0,3], 3: [2,1,0,3], 4: [3,0,1,2]}

# Eye calibration locations
xPositions = [-barSize[1], 0, barSize[1]]
yPositions = [barSize[1], 0, -barSize[1]]
allPositions = list(itertools.product(xPositions, yPositions)) # 9 times x,y coordinates