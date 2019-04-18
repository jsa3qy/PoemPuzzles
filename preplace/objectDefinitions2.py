
import sys

class sylNode:
    #constructor
    def __init__(self, listOfSyls, index, tag, absolutePos):
        self.wordSize = len(listOfSyls)
        self.sylRight = self.wordSize - index - 1
        self.sylLeft = index
        self.tag = tag
        self.syl = listOfSyls[index]
        self.absolutePos = absolutePos

    def toString(self):
        print("word size: " + str(self.wordSize) + "\nsylRight: " + str(self.sylRight) + "\nsylLeft: " + str(self.sylLeft) + "\ntag: " + str(self.tag) + "\nsyl: " + str(self.syl) + "\nabsolutePos: " + str(self.absolutePos) + "\n" )

class ominoe:
    #constructor
    def __init__(self, size):
        self.sylAvailable = size
        self.size = size
        self.sylList = []
        self.reachableIndices = []
        self.valid = True

    #returns a list of ints, which are the indices that make up this ominoe. Useful for debugging
    def getIndicesInOminoe(self):
        tempList = []
        for i in self.sylList:
            tempList.append(i.absolutePos)
        tempList.sort()
        return tempList

    #extends what is reachable in the ominoe based on what is reachable from this index passed
    def extendReachables(self, index, POEM_SIZE):
        listOfSylsSize = POEM_SIZE
        reachablesFromIndex = listOfReachableIndices(index, listOfSylsSize)
        for index in reachablesFromIndex:
            if (index not in self.reachableIndices):
                indexInTile = False
                for node in self.sylList:
                    if index==node.absolutePos:
                        indexInTile = True
                if indexInTile == False:
                    self.reachableIndices.append(index)
    #simply removes the index from the reachables (we shouldn't be able to "reach" what is already a part of us)
    def removeReachables(self, index):
        if (index in self.reachableIndices):
            self.reachableIndices.remove(index)

    #constructs a unique string to hash the piece to so we dont double count tiles
    #specifically it is the ordered indices of the nodes concatinated as a string. tag==index
    def stringToHash(self):
        tempList = []
        for node in self.sylList:
            tempList.append(node.tag)
        tempList.sort()
        tempStr = "".join(tempList)
        return tempStr

    #prints the list of indices in the ominoe, oops basically the same as getIndicesInOminoe()
    def toString(self):
        tempList = []
        for syl in self.sylList:
            tempList.append(syl.absolutePos)
        tempList.sort()
        print(tempList)
        return tempList

#get's the list of reaachable indices from any given index given the size of the poem and the index
def listOfReachableIndices(index, listOfSylsSize):
    #index is index in whole poem, that is, the #syllable
    reachable = []
    if (index%10 != 0):
        reachable.append(index-1)
    if (index%10 != 9):
        reachable.append(index+1)
    if index + 10 < listOfSylsSize:
        reachable.append(index+10)
    if index >= 10:
        reachable.append(index-10)
    return reachable
