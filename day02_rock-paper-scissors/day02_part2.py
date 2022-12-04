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
        case "B":
            return Shape.PAPER
        case "C":
            return Shape.SCISSORS
        case _:
            return None


def getNeededOutcome(input):
    match input:
        case "X":
            return Outcome.Defeat
        case "Y":
            return Outcome.Draw
        case "Z":
            return Outcome.Victory
        case _:
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


def getMyShape(opponentShape, neededOutcome):
    if neededOutcome == Outcome.Draw:
            return opponentShape
    match opponentShape:
        case Shape.ROCK: 
            if neededOutcome == Outcome.Defeat:
                return Shape.SCISSORS
            if neededOutcome == Outcome.Victory:
                return Shape.PAPER
            
        case Shape.PAPER: 
            if neededOutcome == Outcome.Defeat:
                return Shape.ROCK
            if neededOutcome == Outcome.Victory:
                return Shape.SCISSORS
            
        case Shape.SCISSORS: 
            if neededOutcome == Outcome.Defeat:
                return Shape.PAPER
            if neededOutcome == Outcome.Victory:
                return Shape.ROCK
            
        case _: return 



try:
    response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

    myScore = 0
    for line in response.text.splitlines():
        opp, me = line.split()
        opponentShape = getShape(opp)
        neededOutcome = getNeededOutcome(me)
        myShape = getMyShape(opponentShape, neededOutcome)
        
        points = getOutcomePoints(neededOutcome) + getShapePoints(myShape)
        myScore += points
        print(f'Opponent: {opp} Me: {me} Result: {neededOutcome} Points: {points}')

    print(f'My score is: {myScore}')
except:
    print("error")


