

POEM_SIZE = 60

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

    def extendReachables(self, index):
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

    def removeReachables(self, index):
        self.reachableIndices.remove(index)

    def listOfReachableIndices(index, listOfSylsSize):
        #index is index in whole poem, that is, the #syllable
        reachable = []
        if index>0:
            reachable.append(index-1)
        if index<listOfSylsSize-1:
            reachable.append(index+1)
        if index + 10 < listOfSylsSize:
            reachable.append(index+10)
        if index >= 10:
            reachable.append(index-10)
        return reachable
