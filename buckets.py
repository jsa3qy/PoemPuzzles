import copy
from objectDefinitions import *
from operator import itemgetter
import math
import numpy as np

buckets = []

class simpleOminoe:
    def __init__(self, orientations, rawTile):
        self.orientations = orientations
        self.tile = rawTile

class simpleNode:
    def __init__(self, val):
        self.up = None
        self.down = None
        self.right = None
        self.left = None
        self.val = val
        self.seen = False

def placeIntoBuckets(listOfSimpleOminoes):
    buckets.append([listOfSimpleOminoes[0]])
    numBuckets = 0

    for index,ominoe in enumerate(listOfSimpleOminoes):
        if index == 0:
            continue
        added = False
        while (not added):
            if (numBuckets == len(buckets)):
                buckets.append([ominoe])
                added = True
                numBuckets = 0
            elif (numBuckets < len(buckets)) and twoTilesSame(ominoe,buckets[numBuckets][0]):
                buckets[numBuckets].append(ominoe)
                added = True
                numBuckets = 0
                break
            else:
                numBuckets+=1


def twoTilesSame(tile1, tile2):
    orientation1 = tile1.orientations[0]
    for orientation2 in tile2.orientations:
        orientation2Copy = copy.deepcopy(orientation2)
        if sameOrientation(orientation1, orientation2Copy):
            return True
    return False

def showTilesVisually(tile, POEM_SIZE):
    boardTile = np.empty(POEM_SIZE,  dtype='|S6')
    boardTile.flatten()
    for j in range(POEM_SIZE):
        boardTile[j] = "."
    for index in tile:
        if index < POEM_SIZE:
            boardTile[index] = "X"#masterListOfSyllables[index]

    boardTile = np.reshape(boardTile,(POEM_SIZE/10,10))
    print("\n")
    print("Tile: " + str(tile))
    print(boardTile)


def sameOrientation(orientation1, orientation2):
    for node in orientation1:
        boolVal, tempIndex = nodeIsPresent(node, orientation2)
        if boolVal and False:
            print(node.up, orientation2[tempIndex].up)
            print(node.down, orientation2[tempIndex].down)
            print(node.right, orientation2[tempIndex].right)
            print(node.left, orientation2[tempIndex].left)
        if boolVal and (tempIndex >= 0):
            orientation2[tempIndex].seen = True
            continue
        else:
            return False
    return True

def nodeIsPresent(node, orientation):
    upValid = False
    downValid = False
    rightValid = False
    leftValid = False
    for node2 in orientation:
        if ((node.up == None and node2.up == None) or (node.up != None and node2.up != None)) and (node2.seen != True):
            upValid = True
        if ((node.down == None and node2.down == None) or (node.down != None and node2.down != None)) and (node2.seen != True):
            downValid = True
        if ((node.left == None and node2.left == None) or (node.left != None and node2.left != None))and (node2.seen != True):
            leftValid = True
        if ((node.right == None and node2.right == None) or (node.right != None and node2.right != None)) and (node2.seen != True):
            rightValid = True
        if (upValid and downValid and leftValid and rightValid):
            return True, orientation.index(node2)
        else:
            upValid = False
            downValid = False
            rightValid = False
            leftValid = False
    return False, -1

#ouch, we have to find a way to traverse the perimeter
#always going clockwise. That's how this implementation works, could do counter clockwise but it would be a non-trivial switch
def buildSimpleOminoes(listOfRawTiles):
    masterListOfOminoes = []
    for tile in listOfRawTiles:
        listOfSimpleNodes = makeListOfSimpleNodes(tile)
        for i, val in enumerate(listOfSimpleNodes):
            listOfSimpleNodes = addNode(i, listOfSimpleNodes)
        list1 = listOfSimpleNodes
        list2 = rotateClockwise(copy.deepcopy(list1))
        list3 = rotateClockwise(copy.deepcopy(list2))
        list4 = rotateClockwise(copy.deepcopy(list3))
        list5 = flipOminoeOverX(copy.deepcopy(list4))
        list6 = rotateClockwise(copy.deepcopy(list5))
        list7 = rotateClockwise(copy.deepcopy(list6))
        list8 = rotateClockwise(copy.deepcopy(list7))
        listOfOrientations = [list1,list2,list3,list4,list5,list6,list7,list8]
        curOminoe = simpleOminoe(listOfOrientations, tile)
        masterListOfOminoes.append(curOminoe)
    return masterListOfOminoes

def flipOminoeOverX(ominoe):
    for index,node in enumerate(ominoe):
        temp = node.down
        ominoe[index].down = node.up
        ominoe[index].up = temp
    return ominoe

def rotateClockwise(ominoe):
    for index,node in enumerate(ominoe):
        down = node.down
        up = node.up
        left = node.left
        right = node.right
        ominoe[index].up = left
        ominoe[index].left = down
        ominoe[index].down = right
        ominoe[index].right = up
    return ominoe


def addNode(curNodeIndex, tile):
    for i, otherNode in enumerate(tile):
        if i != curNodeIndex:
            if otherNode.val == tile[curNodeIndex].val -10:
                tile[curNodeIndex].up = otherNode
            elif otherNode.val == tile[curNodeIndex].val +10:
                tile[curNodeIndex].down = otherNode
            elif otherNode.val == tile[curNodeIndex].val +1:
                tile[curNodeIndex].right = otherNode
            elif otherNode.val == tile[curNodeIndex].val -1:
                tile[curNodeIndex].left = otherNode
    return tile

def makeListOfSimpleNodes(rawTile):
    newTile = []
    for i in rawTile:
        newNode = simpleNode(i)
        newTile.append(newNode)
    return newTile
