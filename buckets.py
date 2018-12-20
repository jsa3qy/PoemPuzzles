import copy
from objectDefinitions import *
from operator import itemgetter
import math
buckets = {}

#this file is going to contain the code to turn a set of tiles
#into a set of subsets where each subset are tiles with the same
#shape. We want to be able to use the same exact cover implementation
#with the uniqueness of shapes constraint
class simpleOminoe:
    def __init__(self):
        self.up = []
        self.down = []
        self.right = []
        self.left = []
        self.hash = ""

class simpleNode:
    def __init__(self, val):
        self.val = val
        self.seen = False
        self.leftValid = True
        self.rightValid = True
        self.upValid = True
        self.downValid = True
        self.startNode = False

def hashTheOminoes(listOfSimpleOminoes):
    for simpleO in listOfSimpleOminoes:
        if buckets.get(simpleO.hash) == None:
            buckets[simpleO.hash] = [simpleO]
        else:
            buckets.get(simpleO.hash).append(simpleO)
    keys = buckets.keys()
    summation = 0
    for key in keys:
        print(key + " " + str(len(buckets.get(key))))
        summation+=len(buckets.get(key))
    print(summation)
    #print(buckets.keys())

#ouch, we have to find a way to traverse the perimeter
def buildSimpleOminoes(listOfRawTiles):
    masterListOfSimpleOminoes = []
    for tile in listOfRawTiles:
        curOminoeBeforeCopy = simpleOminoe()
        curOminoe = copy.deepcopy(curOminoeBeforeCopy)
        indexOfMax = tile.index(max(tile))
        tileOfNodes = makeATileOfSimpleNodes(tile)
        curNode = tileOfNodes[indexOfMax]
        iCanGoLeft = True
        while iCanGoLeft:
            #if there's another node to our left, AND that node doesn't have a node below it
            if (curNode.val -1 in tile) and (tileOfNodes[tile.index(curNode.val -1)].downValid):
                curNode = tileOfNodes[tile.index(curNode.val -1)]
            else:
                iCanGoLeft = False
                curNode.startNode = True
        #Now we traverse up and go around the whole ominoe, when we try to go up on a node with .startNode == True, we are done
        



def makeATileOfSimpleNodes(tile):
    returnList = []
    for i in tile:
        newNode = simplenode(i)
        if (i-1 in tile):
            newNode.leftValid = False
        if (i+1 in tile):
            newNode.rightValid = False
        if (i+10 in tile):
            newNode.downValid = False
        if (i-10 in tile):
            newNode.upValid = False
        returnList.append(newNode)
    return returnList
