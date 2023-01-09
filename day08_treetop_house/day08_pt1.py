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


try:
    
    response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})
    
    trees = list()

    for line in response.text.splitlines():
        trees.append([ *line ])


    print(f'Total rows: {len(trees)}, total length: {len(trees[0]) if len(trees)>0 else 0}')

    if len(trees)==0:
        raise Exception("No trees") 

    # To count visible trees, we must traverse grid from each of four directions:
    # left-to-right (eastern direction)
    # top-to-bottom (southern direction)
    # right-to-left (western direction)
    # bottom-to-top (northern direction)
    #
    # For each direction, we will go through each sequence of trees (that is, row or column) 
    # from first tree to last one.
    # If the tree height is increasing, then the tree is visible.
    # We will save visible trees in hashtable marking their indexes with boolean True (to mind already visited trees)
    # We will count total visible trees in the process
 
    visibleTrees = dict()
    first_row = trees[0] 
    visibleCounter = 0
    directions = [Directions.EAST, Directions.SOUTH, Directions.WEST, Directions.NORTH]
    for dir in directions:
        rngX = range(len(first_row)-1,-1,-1) if dir == Directions.WEST else range(len(first_row))
        rngY = range(len(trees)-1,-1,-1) if dir == Directions.NORTH else range(len(trees))

        print(f'Direction {dir}.')

        # If we move by Y axis, first traverse X range, then Y 
        if dir in [Directions.NORTH, Directions.SOUTH]:
            rng1 = rngX
            rng2 = rngY
            getPoint = lambda c1, c2: Coord(c1, c2)  
        # If we move by X axis, first traverse Y range, then X
        elif dir in [Directions.EAST, Directions.WEST]:
            rng1 = rngY
            rng2 = rngX
            getPoint = lambda c1, c2: Coord(c2, c1) 

        for c1 in rng1:    
            tallestSoFar = -1
            for c2 in rng2:
                x = getPoint(c1, c2).x
                y = getPoint(c1, c2).y
                curHeight = int(trees[y][x])
                visible = (tallestSoFar < curHeight)
                if visible:
                    tallestSoFar = curHeight
                    if (x,y) not in visibleTrees:                            
                        visibleCounter +=1             
                        visibleTrees[(x,y)] = True

        print(f'Direction {dir}. Number of visible trees so far: {visibleCounter}')

    print(f'Total number of visible outside trees is {visibleCounter}')
    #print(f'Hashtable contains elements: {len(visibleTrees)}')
    my_list = list(visibleTrees)
    my_list.sort()
    print(my_list)
except:
    print("error")



