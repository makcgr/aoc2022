import requests
from enum import Enum

url = "https://adventofcode.com/2022/day/2/input"


SESSIONID = "53616c7465645f5fbefe639536f4494cf0cf8cd653bbab17826e6a37f2b4ee6fc7fa12a606b2419d275e8dc9ecbede1796bae328bf608adc7ab647bf20133600"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"

class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcome(Enum):
    Victory = 1
    Defeat = 2
    Draw = 3    


def getShape(input):
    match input:
        case "A":
            return Shape.ROCK
        case "X":
            return Shape.ROCK
        case "B":
            return Shape.PAPER
        case "Y":
            return Shape.PAPER
        case "C":
            return Shape.SCISSORS
        case "Z":
            return Shape.SCISSORS
        case _:
            return None

def round(me, opp):
    if me == opp:
        return Outcome.Draw
    if me == Shape.PAPER and opp == Shape.ROCK:        
        return Outcome.Victory
    if me == Shape.PAPER and opp == Shape.SCISSORS:        
        return Outcome.Defeat
    if me == Shape.ROCK and opp == Shape.PAPER:        
        return Outcome.Defeat
    if me == Shape.ROCK and opp == Shape.SCISSORS:        
        return Outcome.Victory
    if me == Shape.SCISSORS and opp == Shape.ROCK:        
        return Outcome.Defeat
    if me == Shape.SCISSORS and opp == Shape.PAPER:        
        return Outcome.Victory
    return None


def getOutcomePoints(outcome):
    match outcome:
        case Outcome.Defeat: return 0
        case Outcome.Draw: return 3
        case Outcome.Victory: return 6
        case _: return


def getShapePoints(shape):
    match shape:
        case Shape.ROCK: return 1
        case Shape.PAPER: return 2
        case Shape.SCISSORS: return 3
        case _: return 


try:
    response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

    myScore = 0
    for line in response.text.splitlines():
        opp, me = [ getShape(s) for s in line.split() ]
        
        outcome = round(me, opp)
        points = getOutcomePoints(outcome) + getShapePoints(me)
        myScore += points
        print(f'Opponent: {opp} Me: {me} Result: {outcome} Points: {points}')
        
    print(f'My score is: {myScore}')
except:
    print("error")


