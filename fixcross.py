""" Import packages"""
from psychopy import visual
import time
from math import degrees, atan2

""" Monitor settings """
monitorHZ = 60
monitorSize = [1536,960]
height = 22; distance = 50; vertResolution = 1536 

deg_per_px = degrees(atan2(.5*height, distance)) / (.5*vertResolution) # Calculate the number of degrees that correspond to a single pixel

""" Object settings """
fixSize = int(0.2/deg_per_px); LineWidth = int(0.05/deg_per_px)
backgroundColor = (50/510,50/510,50/510) 

""" Objects """
mywin = visual.Window(
    color = backgroundColor,
    checkTiming = True,
    monitor = "testMonitor", 
    size = monitorSize,
    units = "pix",
    fullscr = True)

fixCross = visual.ShapeStim(
    win = mywin, 
    vertices = ((0,-fixSize), (0,fixSize), (0,0), (-fixSize,0), (fixSize,0)),
    lineWidth = LineWidth,
    closeShape = False,
    units = 'pix')

""" Present a fixation cross """
def presentFix():
    fixCross.setAutoDraw(True) # Draw a fixation cross

    x = time.time()
    for i in range(30):        # Flip 30 times for 500 ms
        mywin.flip()
    y = time.time()
    print(y-x)
    print(print(mywin.monitorFramePeriod))

    fixCross.setAutoDraw(False) # Remove it 

""" Run 10 times """
for i in range(10):
    presentFix()