'''
Created on Sep 2, 2016

@author: frouglas
'''

import csv

class team():
    def __init__(self):
        self.ELO = 0
        self.name = ""
        self.teamID = 0
        self.opponent = []

def parseSched():    
    schedFile = "2016 NFL Schedule Grid - FF Today.txt"
    
    teamNum = 0
    teamIndex = {}
    teamDB = []
    
    with open(schedFile) as schedule:
        thisLine = schedule.readline()
        while thisLine != "":
            for i in range(0,18):
                if i == 0:
                    thisTeam = team()
                    thisTeam.name = thisLine[0:-1]
                    thisTeam.teamID = teamNum
                    teamNum += 1
                    teamIndex[thisTeam.name] = thisTeam.teamID
                else:
                    thisTeam.opponent.append(thisLine[0:-1])
                thisLine = schedule.readline()
            teamDB.append(thisTeam)
    parseResult = [teamIndex, teamDB]
    return parseResult

def parseELO(teamInd, teamD):
    ELOFile = "ELOs.csv"
    with open(ELOFile) as ELORead:
        fileRead = csv.reader(ELORead, delimiter=',')
        for row in fileRead:
            teamD[teamInd[row[0]]].ELO = int(row[1])
    parseResult = [teamInd, teamD]
    return parseResult