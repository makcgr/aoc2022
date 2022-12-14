import requests
from enum import Enum

url = "https://adventofcode.com/2022/day/7/input"


SESSIONID = "53616c7465645f5fbefe639536f4494cf0cf8cd653bbab17826e6a37f2b4ee6fc7fa12a606b2419d275e8dc9ecbede1796bae328bf608adc7ab647bf20133600"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"

class LineMeaning(Enum):
    NONE = 0,
    CHANGE_DIR = 1,
    LS = 2,
    DIR = 3,
    FILE = 4    

class Node(object):
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.parent = None
        self.children = list()
        
    def __str__(self):
      return f"{self.name})"

    def addChild(self, node):
        self.children.append(node)
        node.parent = self

    def addSizeUpwardsRecursive(self, size):
        self.size += int(size)
        cur = self
        while (cur.parent != None):
            cur = cur.parent
            cur.size += int(size)


    def printChildrenRecursive(self):
        cur = self
        print (f'{self.name} {self.size}')
        for node in self.children:
            node.printChildrenRecursive()


    def findNodesLessThan(root, value):
        nodes = list()
        Node.findNodesRecursive(root, nodes, value)
        return nodes


    def findNodesRecursive(node, list, atMost):
        if node.size <= atMost:
            list.append(node)
        for child in node.children:
            Node.findNodesRecursive(child, list, atMost)
        return list


def createSet(startId, finishId):
    return set(range(int(startId), int(finishId)+1))

try:
    response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

    count = 0
    
    cur = None
    root = None
    for line in response.text.splitlines():
        words = line.split()
        meaning = LineMeaning.NONE

        if len(words)<2:
            continue
        elif len(words)==2:
            if (words[1] == "ls"):
                meaning = LineMeaning.LS
            elif (words[0] == "dir"):
                meaning = LineMeaning.DIR
            elif (words[0].isnumeric()):
                meaning = LineMeaning.FILE
        elif len(words)==3:
            if words[1] == "cd":
                meaning = LineMeaning.CHANGE_DIR
        
        if meaning==LineMeaning.CHANGE_DIR:
            isUp = words[2] == ".."
            if isUp:
                if cur == None:
                    raise Exception("cd .. but cur is None")
                else:
                    if cur.parent != None:
                        cur = cur.parent
                    else:
                        raise Exception("cd .. but cur has no Parent!")
            else:
                directory = words[2]
                newNode = Node(directory)
                if directory == "/":
                    root = newNode

                if cur == None:
                    cur = newNode
                else:
                    cur.addChild(newNode)
                    newNode.parent = cur
                    cur = newNode
                
        elif meaning==LineMeaning.FILE:
            if cur != None:
                filesize = int(words[0])
                cur.addSizeUpwardsRecursive(filesize)
            else:
                raise Exception("line meaning is file info, but cur is None!")       

        #print(f'{words}')

        # skip ls
    
    if root != None:
        root.printChildrenRecursive()
        atMost = 100000
        #sum = Node.findSumRecursive(root, 0, atMost)
        nodes = Node.findNodesLessThan(root, atMost)
        sum = 0
        for node in nodes:
            sum += node.size
        print(sum)

except:
    print("error")


