'''
Created on Sep 2, 2016

@author: frouglas
'''

from schedParse import *
import math
from random import randint, random
from pycparser.c_ast import Goto

def compileSched(teamDB, teamList, startWk):
    
    homeAdv = 65
    weeklyFaves = []
    
    for i in range(startWk,17):
        favorites = []
        teamsMatched = []
        for j in teamDB:
            if j.teamID in teamsMatched:
                continue
            else:
                oppTeam = j.opponent[i]
                if oppTeam == "Bye":
                    continue
                if oppTeam[0] == "@":
                    oppTeam = oppTeam[1:]
                    home = 0
                else:
                    home = 1
                oppTeamID = teamList[oppTeam]
                teamsMatched.append(j.teamID)
                teamsMatched.append(oppTeamID)
                teamELO = j.ELO
                oppELO = teamDB[oppTeamID].ELO
                if home == 1:
                    teamELO += homeAdv
                else:
                    oppELO += homeAdv
                if teamELO>oppELO:
                    winProb = ELOProb(teamELO,oppELO)
                    favorites.append([j.teamID,winProb])
                elif oppELO>teamELO:
                    winProb = ELOProb(oppELO,teamELO)
                    favorites.append([oppTeamID,winProb])
        weeklyFaves.append(favorites)
    return weeklyFaves

def ELOProb(favELO,oppELO):
    ELODiff = favELO - oppELO
    ELOPower = 10**(-float(ELODiff)/400)
    prob = 1/(ELOPower+1)
    return prob

def runElim(weeklyFaves, picks):
    
    newPicks = []
    for weekFaves in weeklyFaves:
        thisPick = randint(0,len(weekFaves)-1)
#        if thisPick == 0:
#            print "        randint returned 0"
#        elif thisPick == len(weekFaves)-1:
#            print "        randint returned " + str(thisPick)
        try:
            while weekFaves[thisPick][0] in picks:
                thisPick = randint(0,len(weekFaves)-1)
        except IndexError:
            print(str(thisPick) + " caused an error")
        newPicks.append(weekFaves[thisPick][0])
        thisProb= random()
        if weekFaves[thisPick][1] <= thisProb:
            break
    return newPicks