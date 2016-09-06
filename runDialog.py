'''
Created on Sep 3, 2016

@author: frouglas
'''

from schedParse import *
from simulator import *
import pickle

usePicks = input("would you like to use an existing set of picks? ")
if usePicks == "y":
    lockedPicks = pickle.load("pickList.list")
    startWk = len(lockedPicks)
else:
    lockedPicks = []
    startWk = 0

sims = 100000

initRun = parseSched()

teamList = initRun[0]
teamDB = initRun[1]

initRun = parseELO(teamList,teamDB)
teamDB = initRun[1]

weeklyFaves = compileSched(teamDB,teamList,startWk)

lengthList = [[] for i in range(0,17)]
teamList = [[] for i in range(0,len(teamList))]
completes = [0 for i in range(0,len(teamList))]

for i in range(0,sims):
    if (float(i)+1)/500000 == int((i+1)/500000):
        print("    processed through " + str(i+1) + " iterations")
    simPicks = runElim(weeklyFaves, lockedPicks)
    thisPick = simPicks[0]
    thisTeam = teamDB[thisPick].name
    thisElim = len(simPicks)
#    print "    in this iteration, " + thisTeam + " was selected for the current week."
#    print "    weeks until failure: " + str(thisElim)
#    print "--------"
    lengthList[thisElim-1].append(thisPick)
    teamList[thisPick].append(thisElim)
    if thisElim == 17:
        completes[thisPick] += 1
        
bestPick = -1
bestPickCompletes = 0
pick2 = -1
pick2Completes = 0
pick3 = -1
pick3Completes = 0

for i in range(0,len(completes)):
    if completes[i] >= bestPickCompletes:
        pick3 = pick2
        pick3Completes = pick2Completes
        pick2 = bestPick
        pick2Completes = bestPickCompletes
        bestPick = i
        bestPickCompletes = completes[i]
    elif completes[i] >= pick2Completes:
        pick3 = pick2
        pick3Completes = pick2Completes
        pick2 = i
        pick2Completes = completes[i]
    elif completes[i] >= pick3Completes:
        pick3 = i
        pick3Completes = completes[i]


bestTeam = teamDB[bestPick].name
team2 = teamDB[pick2].name
team3 = teamDB[pick3].name

print "the best pick for the current week is " + bestTeam + ", leading to " + str(bestPickCompletes) + " successful elimination seasons"
print "    the 2nd best pick for the current week is " + team2 + ", leading to " + str(pick2Completes) + " successful elimination seasons"
print "    the 3rd best pick for the current week is " + team3 + ", leading to " + str(pick3Completes) + " successful elimination seasons"

currPick = input("which team would you like to select? ")
if currPick == 1:
    lockedPicks.append(bestPick)
elif currPick == 2:
    lockedPicks.append(pick2)
elif currPick == 3:
    lockedPicks.append(pick3)

pickle.dump("pickList.list")