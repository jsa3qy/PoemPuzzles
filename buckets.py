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
        for index, outerVal in enumerate(tile):
            if outerVal+1 not in tile:
                curOminoe.right.append()
    return masterListOfSimpleOminoes
