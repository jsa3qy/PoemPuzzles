from dataCleaningHelpers import *
from tilingHelpers import *
from objectDefinitions import *
from test import *
from setCover import *
import numpy as np
import random
import exact_cover_np as ec
from buckets import *
import sys


OMINOE_SIZE = 5
POEM_SIZE = 60
def main():
    myFile = open("poem.txt")
    #otherFile = open("syllablizedPoemOneSyllablePerWord.txt")
    otherFile = open("syllablizedPoem.txt")
    #No punctuation in words!
    listOfWords = readInRawPoem(myFile)
    listOfSyls = readInSyllablePoem(otherFile)
    masterListOfSyllables = makeMasterListOfSyllables(listOfSyls)
    listOfSylNodes = makeSylNodes(listOfSyls)

    for i, node in enumerate(listOfSylNodes):
        #AHHH CAN BE OPTIMIZED WITH TRIES OVER HASHMAP
        myOminoe = ominoe(OMINOE_SIZE)
        myOminoe.reachableIndices+= listOfReachableIndices(i, POEM_SIZE)
        extendOminoe(myOminoe, i, listOfSylNodes)
        expandInAllDirections(myOminoe, listOfSylNodes)

    #let's take valid tiles from the ominoe objects and sort them
    sortedListOfTiles = []
    for validTile in listOfTiles:
        sortedListOfTiles.append(validTile.getIndicesInOminoe())

    builtListOfSimpleOminoes = buildSimpleOminoes(sortedListOfTiles)
    placeIntoBuckets(builtListOfSimpleOminoes)

    validCount = 0
    sortedListOfTilesCopy = copy.deepcopy(sortedListOfTiles)
    for i in range(1):
        cover = []
        counter = 0
        while (len(cover) == 0):
            counter+=1
            if counter%10 == 0:
                print(counter)
            sortedListOfTiles = []
            numPadding = POEM_SIZE/OMINOE_SIZE
            if (int(numPadding) != POEM_SIZE/OMINOE_SIZE):
                print("not possible")
                sys.exit(1)
            chosenBuckets = random.sample(range(0, len(buckets)), numPadding)
            #print("chosen buckets:",chosenBuckets)
            #print("number of buckets:", len(buckets))
            bucketAddition = POEM_SIZE
            for i,bucket in enumerate(buckets):
                if (i in chosenBuckets):
                    for ominoeObject in bucket:
                        tempTile = ominoeObject.tile
                        tempTile.append(bucketAddition)
                        sortedListOfTiles.append(tempTile)
                    bucketAddition +=1
            rangeIncrease = numPadding
            #print(sortedListOfTiles)
            #sortedListOfTiles.sort(key=lambda x: x[0])
            random.shuffle(sortedListOfTiles)
            true = 0
            #print("Done with tile enumeration, finding a valid tiling!")
            #print("num tiles: " + str(len(sortedListOfTiles)))
            #exact cover time
            listOfUsableInputs = []
            for tile in sortedListOfTiles:
                referenceTile = np.zeros(POEM_SIZE+rangeIncrease)
                for index in tile:
                    referenceTile[index] += 1
                listOfUsableInputs.append(referenceTile)
            S = np.array(listOfUsableInputs, dtype='int32')
            cover = ec.get_exact_cover(S)

        finalList = []
        for i in cover:
            finalList.append(sortedListOfTiles[i])

        check = np.zeros(POEM_SIZE+rangeIncrease)
        for tile in finalList:
            for val in tile:
                check[val]+=1
        valid = True
        for i, val in enumerate(check):
            if val != 1:
                valid = False
        if valid:
            validCount+=1
            for i in finalList:
                print(i)
            print('\n')
    print(validCount)
    for indexT, tile in enumerate(finalList):
        boardTile = np.empty(POEM_SIZE,  dtype='|S6')
        boardTile.flatten()
        for j in range(POEM_SIZE):
            boardTile[j] = "."
        for index in tile:
            if index < POEM_SIZE:
                boardTile[index] = "X"#masterListOfSyllables[index]

        boardTile = np.reshape(boardTile,(6,10))
        print("\n")
        print("Tile: " + str(tile))
        print("Tile Number:" + str(indexT))
        print(boardTile)


if __name__ == "__main__":
    main()
