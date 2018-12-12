from objectDefinitions import *
import copy
import math

touchPieces = []

#this function will tell us if a tile is valid. It takes in a list of indices, sorts them based on the number of other reachableIndices it touches, and then uses the min of those as a starting point, calling a recursive function to validate all indices it can reach. This is slow but good, and I havent found a case where it breaks yet.
def testForValidity(ListOfValsInOminoe):
        tempOminoe = copy.deepcopy(ListOfValsInOminoe)
        arrayOfCorrespondingIndicesTouched = []
        tempCount = 0
        for i, val in enumerate(tempOminoe):
            for j in range(0, len(tempOminoe)):
                if (i!=j):
                    if (isAdjacent(val, tempOminoe[j])):
                        tempCount+=1
            if (tempCount == 0):
    
                return False
            arrayOfCorrespondingIndicesTouched.append(tempCount)
            tempCount=0

        for i,val in enumerate(tempOminoe):
            touchPieces.append(touchPiece(arrayOfCorrespondingIndicesTouched[i],val))
        touchPieces.sort(key= lambda touchPiece: touchPiece.numTouching)
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
class touchPiece:
    def __init__(self, numTouching, index):
        self.numTouching = numTouching
        self.index = index
        self.seen = False
