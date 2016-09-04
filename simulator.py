'''
Created on Sep 2, 2016

@author: frouglas
'''

from schedParse import *

homeAdv = 65

initRun = parseSched()

teamList = initRun[0]
teamDB = initRun[1]

initRun = parseELO(teamList,teamDB)

breakHere = 1

