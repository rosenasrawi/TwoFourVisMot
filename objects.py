""" Import packages"""

from psychopy import visual
from psychopy.hardware import keyboard

""" Import configuration parameters """

from parameters import *

""" Window & Keyboard """

mywin = visual.Window(
    color = backgroundColor,
    monitor = "testMonitor", 
    size = monitorSize,
    units = "pix",
    fullscr = True)

kb = keyboard.Keyboard()

mouse = visual.CustomMouse(
    win = mywin,
    visible = False)

""" Fixation """

fixCross = visual.ShapeStim(
    win = mywin, 
    vertices = ((0,-fixSize), (0,fixSize), (0,0), (-fixSize,0), (fixSize,0)),
    lineWidth = LineWidth,
    closeShape = False,
    units = 'pix')

""" Bars """

leftBarTop = visual.Rect(
    win = mywin,
    units = "pix",
    width = barSize[0],
    height = barSize[1],
    pos = leftBarTopPos)

rightBarTop = visual.Rect(
    win = mywin,
    units = "pix",
    width = barSize[0],
    height = barSize[1],
    pos = rightBarTopPos)

leftBarBot = visual.Rect(
    win = mywin,
    units = "pix",
    width = barSize[0],
    height = barSize[1],
    pos = leftBarBotPos)

rightBarBot = visual.Rect(
    win = mywin,
    units = "pix",
    width = barSize[0],
    height = barSize[1],
    pos = rightBarBotPos)

""" Response dial """

responseCircle = visual.Circle(
    win = mywin,
    radius = circleRadius,
    edges = circleEdges,
    lineWidth = LineWidth,
    lineColor = fixColor)

turnUpper = visual.Circle( 
    win = mywin,
    radius = miniCircleRadius,
    edges = circleEdges,
    lineWidth = LineWidth,
    fillColor = backgroundColor,
    lineColor = fixColor)

turnLower = visual.Circle( 
    win = mywin,
    radius = miniCircleRadius,
    edges = circleEdges,
    lineWidth = LineWidth,
    fillColor = backgroundColor,
    lineColor = fixColor)

""" Text """

feedbackText = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = '',
    color = fontColor,
    pos = [0,2*fixSize],
    height = fontSizeFeedback)
    

# Precues

# Load
precueTextColor = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "Relevant colors this block:",
    color = fontColor,
    pos = [0,2*barSize[1]],
    height = fontSizePreCue)

# Middle 
precueColors0 = visual.TextStim(    
    win = mywin, 
    font = textFont,
    text = "&",
    pos = fixPos,
    height = fontSizePreCue)

# Quadrant in load 4
precueColors4a = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "",
    pos = leftBarTopPos,
    height = fontSizePreCue)

precueColors4b = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "",
    pos = rightBarTopPos,
    height = fontSizePreCue)

precueColors4c = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "",
    pos = leftBarBotPos,
    height = fontSizePreCue)

precueColors4d = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "",
    pos = rightBarBotPos,
    height = fontSizePreCue)

# On two sides in load 2

precueColors2a = visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "",
    pos = leftBarPos,
    height = fontSizePreCue)

precueColors2b =  visual.TextStim(
    win = mywin, 
    font = textFont,
    text = "",
    pos = rightBarPos,
    height = fontSizePreCue)
