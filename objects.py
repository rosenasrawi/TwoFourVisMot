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
    