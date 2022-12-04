import requests
from enum import Enum

url = "https://adventofcode.com/2022/day/3/input"

SESSIONID = "53616c7465645f5fbefe639536f4494cf0cf8cd653bbab17826e6a37f2b4ee6fc7fa12a606b2419d275e8dc9ecbede1796bae328bf608adc7ab647bf20133600"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"


def getPrio(item):
    if ord('A') <= ord(item) and ord(item) < ord('a'):
        return 27 + ord(item) - ord('A')
    if ord(item) >= ord('a'):
        return ord(item) - ord('a') + 1


def processRucksack(sack, groupdict):
    sackDict = dict()
    isFirstElf = len(groupdict)==0
    for c in sack:
        if isFirstElf:
            groupdict[c] = 1
        elif c in groupdict and c not in sackDict:
            sackDict[c] = True
            groupdict[c] += 1
            if groupdict[c] >= 3:
                return getPrio(c)
    return 0
        

try:
    response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})
    prioSum = 0
    groupCounter = 0
    groupdict = None
    for line in response.text.splitlines():
        if groupCounter == 0:
            groupdict = dict()
        
        groupCounter +=1
        groupPrio = processRucksack(line, groupdict)

        if groupCounter==3:
            prioSum += groupPrio
            groupCounter = 0          
        
    print(prioSum)
except:
    print("error")
