""" Import packages"""

from psychopy import parallel, serial, core, event
from eyelinkPackages import eyelinker
import os

""" Import other task scripts """

from parameters import monitorHZ, portType, eyeDirectory
from objects import mywin, eyecalibrationWaitText, eyecalibrationSaveText

""" EEG """

# Parallel port 
if portType == 'parallel':

    # Create connection with port (parallel or serial)
    def connectEEG():
        portEEG = parallel.ParallelPort(address = 0x3050)
        portEEG.setData(0)
        
        return portEEG

# Serial port
elif portType == 'serial':

    # Create connection with port (parallel or serial)
    def connectEEG():
        portEEG = serial.Serial(
            port = 'COM7', baudrate = 115200,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS)

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
