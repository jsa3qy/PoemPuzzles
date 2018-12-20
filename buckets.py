import copy
from objectDefinitions import *
buckets = {}

#this file is going to contain the code to turn a set of tiles
#into a set of subsets where each subset are tiles with the same
#shape. We want to be able to use the same exact cover implementation
#with the uniqueness of shapes constraint
class simpleOminoe:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.finalList = []
        self.hash = ""

class simpleNode:
    def __init__(self, val):
        self.val = val
        self.seen = False

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
    print(buckets.keys())
#takes list of lists which are just the indices of the tiles and returns simple ominoes
#ready to hash into buckets
def buildSimpleOminoes(listOfRawTiles):
    listOfSimpleOminoes = []
    for tile in listOfRawTiles:
        tempOminoe = simpleOminoe()
        tempTile = []
        for i in tile:
            tempTile.append(simpleNode(i))
        tempTile[0].seen = True
        evaluateType(tempOminoe, 0, tempTile)
        listOfSimpleOminoes.append(tempOminoe)
    for simpleO in listOfSimpleOminoes:
        tempList = []
        tempList.append(simpleO.up)
        tempList.append(simpleO.down)
        tempList.append(simpleO.left)
        tempList.append(simpleO.right)
        tempList.sort()
        simpleO.finalList = tempList
        simpleO.hash = ".".join(str(x) for x in tempList)
    return listOfSimpleOminoes

#this will be a recursive function which records how we do our breadth first search in the ominoe object
def evaluateType(ominoe, index, tile):
    #tile = copy.deepcopy(tile2)
    #look through ominoe recording every movement
    for i,index2 in enumerate(tile):

        if index2.val == index+10:
            ominoe.down+=1
        elif index2.val == index-10:
            ominoe.up+=1
        elif index2.val == index+1:
            ominoe.right+=1
        elif index2.val == index-1:
            ominoe.left+=1
        if (not index2.seen):
            tile[i].seen = True
            evaluateType(ominoe, index2.val, tile)
