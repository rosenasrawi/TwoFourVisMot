""" Import packages"""

import os, csv
from datetime import datetime

""" Import data directory """

from parameters import dataDirectory

""" Create new logfile """

def newLogfile():
    os.chdir(dataDirectory)
    
    subjectID = input('Subject ID (01, 02, ...): ')
    session = input('Current session (a, b): ') 
    now = datetime.now(); now = now.strftime('%m%d%Y_%H%M%S')

    filename = 'rn4_s' + subjectID + session + '_' + now + '.csv'
    header = ['leftBarTopOri',                 
              'rightBarTopOri',
              'leftBarBotOri', 
              'rightBarBotOri',
              'leftBarTopCol',                 
              'rightBarTopCol',
              'leftBarBotCol', 
              'rightBarBotCol',               
              'targetCol', 
              'targetLocation',
              'targetOri',
              'reportOri',
              'circleSteps', 
              'clockwise',
              'difference', 
              'performance',
              'fixTime', 
              'probeTime',
              'pressTime', 
              'releaseTime', 
              'responseTime', 
              'responseDur',
              'dialType', 
              'loadType', 
              'trialType',
              'blockNum',
              'encTrig',
              'probeTrig', 
              'respTrig']

    with open(filename, mode = 'w') as datafile:
        writer = csv.DictWriter(datafile, delimiter = ',', fieldnames = header)
        writer.writeheader()

    return filename, header, subjectID, session

""" Create trialdata dict """

def createTrialData(leftBarTop, rightBarTop, leftBarBot, rightBarBot, targetCol, 
                    thisTargetLoc, targetOri, reportOri, count, clockwise, difference,
                    performance, thisFixTime, probeTime, pressTime, releaseTime,
                    dialType, loadType, trialType, thisBlockNum, encTrig, probeTrig, respTrig):

    # Create trialdata
    trialData = {'leftBarTopOri':   leftBarTop.ori,                 
                 'rightBarTopOri':  rightBarTop.ori,
                 'leftBarBotOri':   leftBarBot.ori, 
                 'rightBarBotOri':  rightBarBot.ori,
                 'leftBarTopCol':   leftBarTop.name,                 
                 'rightBarTopCol':  rightBarTop.name,
                 'leftBarBotCol':   leftBarBot.name, 
                 'rightBarBotCol':  rightBarBot.name,               
                 'targetCol':       targetCol, 
                 'targetLocation':  thisTargetLoc,
                 'targetOri':       round(targetOri),
                 'reportOri':       round(reportOri),
                 'circleSteps':     count, 
                 'clockwise':       clockwise,
                 'difference':      difference, 
                 'performance':     performance,
                 'fixTime':         thisFixTime, 
                 'probeTime':       probeTime,
                 'pressTime':       pressTime, 
                 'releaseTime':     releaseTime, 
                 'responseTime':    pressTime - probeTime, 
                 'responseDur':     releaseTime - pressTime,
                 'dialType':        dialType, 
                 'loadType':        loadType, 
                 'trialType':       trialType,
                 'blockNum':        thisBlockNum,
                 'encTrig':         encTrig,
                 'probeTrig':       probeTrig, 
                 'respTrig':        respTrig}

    return trialData

""" Add trial to logfile """

def addTrialLogfile(filename, header, trialData):
    os.chdir(dataDirectory)
    
    with open(filename, mode = 'a', newline = '') as datafile:
        writer = csv.DictWriter(datafile, fieldnames = header)
        writer.writerow(trialData)