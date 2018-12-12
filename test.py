from objectDefinitions import *
import copy
import math

touchPieces = []

#this function will tell us if a tile is valid. It takes in a list of indices, sorts them based on the number of other reachableIndices it touches, and then uses the min of those as a starting point, calling a recursive function to validate all indices it can reach. This is slow but good, and I havent found a case where it breaks yet.
def testForValidity(ListOfValsInOminoe):
        tempOminoe = copy.deepcopy(ListOfValsInOminoe)
        arrayOfCorrespondingIndicesTouched = []
        for i,val in enumerate(tempOminoe):
            touchPieces.append(touchPiece(val))
        startPoint = touchPieces[0]
        markAllAdjacent(startPoint.index)
        for i in touchPieces:
            if i.seen == False:
                touchPieces.clear()
                return False
        touchPieces.clear()
        return True

def markAllAdjacent(index):
    for i, val in enumerate(touchPieces):
        if (isAdjacent(val.index, index) and val.seen == False):
            touchPieces[i].seen = True
            markAllAdjacent(touchPieces[i].index)
    return

def isAdjacent(num1, num2):
    if ((math.fabs(num1 - num2) == 1) or (math.fabs(num1 - num2) == 10)):
        if (not ((num1%10 == 0 and num2%10 == 9) or (num1%10 == 9 and num2%10 == 0))):
            return True

    return False

#specifically what's wrong is that the reachable indices do not match the indices that are in the ominoe
def somethingWrongHere(ominoe):
    somethingWrong = False
    for i, val in enumerate(ominoe.reachableIndices):
        adjacent = False
        for j, val2 in enumerate(ominoe.getIndicesInOminoe()):
            if (isAdjacent(val, val2)):
                adjacent = True
        if adjacent == False:
            somethingWrong = True
    return somethingWrong

class touchPiece:
    def __init__(self, numTouching, index):
        self.index = index
        self.seen = False
