import copy

class tileObject:
    def __init__(self, tile):
        self.ogtile = copy.deepcopy(tile)
        self.leftMostPosition = copy.deepcopy(tile)
        self.currentPosition = tile

class tileDescriptor:
    def __init__(self, tile, bucketNum, POEM_SIZE = 80):
        self.rawTile = tile
        self.binaryTile = [0]*POEM_SIZE
        for i in tile:
            self.binaryTile[i] = 1
        self.bucketNum = bucketNum
    def toString(self, specifier):
        if specifier == 0:
            print("rawTile: ", self.rawTile)
            print("binaryTile: ", self.binaryTile)
            print("bucketNum: " + str(self.bucketNum))
        if specifier == 1:
            print("rawTile: ", self.rawTile)
            print("bucketNum: " + str(self.bucketNum))
        if specifier == 2:
            print("rawTile: ", self.rawTile)
            print("bucketNum: " + str(self.bucketNum))
    def toStringWord(self, listOfNodes):
        for i in self.rawTile:

            print(listOfNodes[i].syl + " " + str(listOfNodes[i].absolutePos) + " " + str(i))
        print("")
