import requests
from enum import Enum

day = 8
url = f'https://adventofcode.com/2022/day/{day}/input'

SESSIONID = "53616c7465645f5fbefe639536f4494cf0cf8cd653bbab17826e6a37f2b4ee6fc7fa12a606b2419d275e8dc9ecbede1796bae328bf608adc7ab647bf20133600"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"


def createSet(startId, finishId):
    return set(range(int(startId), int(finishId)+1))


class Directions(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Coord:
    def __init__(self, x, y): 
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'


def GetNextCoord(coord, dir):
    if dir == Directions.EAST:
        x = coord.x + 1
        y = coord.y
    elif dir == Directions.WEST:
        x = coord.x - 1
        y = coord.y
    elif dir == Directions.NORTH:
        x = coord.x
        y = coord.y - 1
    elif dir == Directions.SOUTH:
        x = coord.x
        y = coord.y + 1
    return Coord(x,y)


def IsValidCoord(coord, trees):
    return coord.x >= 0 and coord.y >= 0 and coord.x < len(trees[0]) and coord.y < len(trees)


def FindVisibility(coord, trees):

    directions = [Directions.EAST, Directions.SOUTH, Directions.WEST, Directions.NORTH]
    visIndex = 1
    for dir in directions:
        initialHeight = int(trees[coord.y][coord.x])
        visIndex *= FindVisRecurse(coord, initialHeight, dir, trees, 0)
    return visIndex


def FindVisRecurse(coord, initialHeight, dir, trees, curVis):
    curHeight = int(trees[coord.y][coord.x]) 
    nextCoord = GetNextCoord(coord, dir)
    if IsValidCoord(nextCoord, trees):
        curVis += 1
        height = int(trees[nextCoord.y][nextCoord.x]) 
        if height >= initialHeight:
            return curVis
        else:
            return FindVisRecurse(nextCoord, initialHeight, dir, trees, curVis)
    else:
        return curVis


try:
    trees = list()
    
    response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})
    for line in response.text.splitlines():
       trees.append([ *line ])

#     uncomment lines below to test on small input:
#     test_input = """30373
# 25512
# 65332
# 33549
# 35390"""
#     for line in test_input.splitlines():
#         trees.append([ *line ])

    print(f'Total rows: {len(trees)}, total length: {len(trees[0]) if len(trees)>0 else 0}')

    if len(trees)==0:
        raise Exception("No trees") 

    visibleTrees = dict()
    first_row = trees[0]

    maxVI = 0
    coordMaxVI = None
    for x in range(len(first_row)):
        for y in range(len(trees)):
            vi = FindVisibility(Coord(x,y), trees)
            if maxVI < vi:
                maxVI = vi
                coordMaxVI = Coord(x,y)
    print(f'Coord: ({coordMaxVI.x},{coordMaxVI.y}) has max Visibility index: {maxVI}')
except:
    print("error")
