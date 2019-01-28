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
from string import ascii_uppercase

#12 pentominoes and 5 tetrominoes
#12 types of pentominoes, 30 types of hexominoes, 76 types of septominoes
#^^ wrong, there are 35 hexominoes 
OMINOE_SIZE = 5
POEM_SIZE = 60

def main():
    bucketsHashMap = {}
    if POEM_SIZE%OMINOE_SIZE != 0:
        print("NOT A POSSIBLE TILING")
        sys.exit(1)
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
    print("done expanding...")
    #let's take valid tiles from the ominoe objects and sort them
    sortedListOfTiles = []
    for validTile in listOfTiles:
        sortedListOfTiles.append(validTile.getIndicesInOminoe())
    print("building simple ominoes")
    builtListOfSimpleOminoes = buildSimpleOminoes(sortedListOfTiles)
    print("built simple ominoes")
    print(len(sortedListOfTiles))
    placeIntoBuckets(builtListOfSimpleOminoes)
    print("number of different ominoes:",len(buckets))

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
            chosenBuckets.sort()
            tempString = ""
            for i in chosenBuckets:
                tempString+=str(i)
            if bucketsHashMap.get(tempString) != None:
                continue
            else:
                bucketsHashMap[tempString] = 1

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
        else:
            print("invalid tiling")
            #sys.exit(1)

    finalListToDisplay = []
    boardTile = np.empty(POEM_SIZE,  dtype='|S6')
    boardTile.flatten()
    for index, val in enumerate(boardTile):
        boardTile[index] = ''
    letterIndex = 0

    for indexT, tile in enumerate(finalList):
        for index in tile:
            if index < POEM_SIZE:
                boardTile[index] = ascii_uppercase[letterIndex]
        letterIndex+=1

    boardTile = np.reshape(boardTile,(6,10))
    print(boardTile)




if __name__ == "__main__":
    main()
