""" Import packages"""

from psychopy import parallel, event
from eyelinkPackages import eyelinker
import os

""" Import other task scripts """

from parameters import eyeDirectory
from objects import mywin, eyecalibrationWaitText, eyecalibrationSaveText

""" EEG """

def connectEEG():
    portEEG = parallel.ParallelPort(address = 0x3050)
    portEEG.setData(0)
    
    return portEEG

""" Eye-tracker """

def connectTracker(subjectID, session):
    tracker = eyelinker.EyeLinker(window = mywin, eye = 'BOTH',
                                  filename = 'rn4_' + subjectID + session + '.edf')
                                      
    return tracker

def startTracker(tracker):
    os.chdir(eyeDirectory)

    tracker.open_edf() # open a data file
    tracker.init_tracker()
    tracker.start_recording()

def calibrateTracker(tracker):
    tracker.stop_recording()

    eyecalibrationWaitText.draw()
    mywin.flip()
    event.waitKeys(keyList = 'R')
    
    tracker.start_recording()

def stopTracker(tracker):
    os.chdir(eyeDirectory)

    eyecalibrationSaveText.draw()

    tracker.stop_recording()
    tracker.transfer_edf()
    tracker.close_edf()
