from dataCleaningHelpers import *
from tilingHelpers import *
from objectDefinitions import *
from test import *

def main():
    myFile = open("poem.txt")
    otherFile = open("syllablizedPoem.txt")

    #No punctuation in words!
    listOfWords = readInRawPoem(myFile)
    listOfSyls = readInSyllablePoem(otherFile)
    masterListOfSyllables = makeMasterListOfSyllables(listOfSyls)
    listOfSylNodes = makeSylNodes(listOfSyls)

    for i, node in enumerate(listOfSylNodes):
        #AHHH CAN BE OPTIMIZED WITH TRIES OVER HASHMAP
        myOminoe = ominoe(5)
        myOminoe.reachableIndices+= listOfReachableIndices(i, 60)
        extendOminoe(myOminoe, i, listOfSylNodes)
        expandInAllDirections(myOminoe, listOfSylNodes)

    #let's take valid tiles from the ominoe objects and sort them
    sortedListOfTiles = []
    for validTile in listOfTiles:
        sortedListOfTiles.append(validTile.getTile())

    sortedListOfTiles.sort(key=lambda x: x[0])
    true = 0
    for validTile in sortedListOfTiles:
        valid = testForValidity(validTile)
        if valid:
            true+=1
        if valid:
            print("valid: ",validTile)
        else:
            print("invalid: ", validTile)
    print("total tiles enumerated: " + str(len(sortedListOfTiles)))
    print("valid tiles: " + str(true))




if __name__ == "__main__":
    main()
