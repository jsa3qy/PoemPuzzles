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
from uniqueness import uniqueCover

#12 pentominoes and 5 tetrominoes
#12 types of pentominoes, 30 types of hexominoes, 76 types of septominoes
#^^ wrong, there are 35 hexominoes
OMINOE_SIZE = [4, 5]
POEM_SIZE = 80
TILINGS_TO_PRINT = 10


def main():

    user_specify = raw_input("Would you like to specify the number of tilings? default is 1 (n/Y): ")
    if user_specify == "Y":
        TILINGS_TO_PRINT = raw_input("How many iterations: ")
        TILINGS_TO_PRINT = int(TILINGS_TO_PRINT)
    elif user_specify == "n":
        print("Running 1 time...")
    else:
        print("invalid response, run program again.")
        sys.exit(1)

    OMINOE_SIZE.sort()
    bucketsHashMap = {}
    #if POEM_SIZE%OMINOE_SIZE != 0:
        #print("NOT A POSSIBLE TILING")
        #sys.exit(1)
    myFile = open("poem.txt")
    otherFile = open("howILoveThee.txt")
    #otherFile = open("syllablizedPoemOneSyllablePerWord.txt")
    #otherFile = open("syllablizedPoem.txt")
    #No punctuation in words!
    listOfWords = readInRawPoem(myFile)
    listOfSyls = readInSyllablePoem(otherFile)
    masterListOfSyllables = makeMasterListOfSyllables(listOfSyls)

    listOfSylNodes = makeSylNodes(listOfSyls)

    for j in OMINOE_SIZE:
        for i, node in enumerate(listOfSylNodes):
            #AHHH CAN BE OPTIMIZED WITH TRIES OVER HASHMAP
            myOminoe = ominoe(j)
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
    print("Number of tiles: " + str(len(sortedListOfTiles)))
    placeIntoBuckets(builtListOfSimpleOminoes)
    print("number of different ominoes:",len(buckets))

    validCount = 0
    sortedListOfTilesCopy = copy.deepcopy(sortedListOfTiles)
    notUniqueCount = 0
    for qqq in range(TILINGS_TO_PRINT):
        cover = []
        #counter = 0
        #if (qqq < TILINGS_TO_PRINT):
            #counter+=1
            #if counter%10 == 0:
                #print(counter)

        #numPadding = POEM_SIZE/OMINOE_SIZE
        numPadding = len(buckets)
        #if (int(numPadding) != POEM_SIZE/OMINOE_SIZE):
            #print("not possible")
            #sys.exit(1)
        if qqq == 0:
            sortedListOfTiles = []
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
#####
        finalList = []
        for i in cover:
            finalList.append(sortedListOfTiles[i])

        if uniqueCover(finalList):
            check = np.zeros(POEM_SIZE+rangeIncrease)
            for tile in finalList:
                for val in tile:
                    check[val]+=1
            valid = True
            for i, val in enumerate(check):
                if val != 1:
                    valid = False
            if valid or not valid:
                validCount+=1
                #for i in finalList:
                    #print(i)
                    #showTilesVisually(i, POEM_SIZE)
                #print('\n')
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

            boardTile = np.reshape(boardTile,(POEM_SIZE/10,10))
            print(str(qqq) + ": ")
            print(boardTile)
        else:
            notUniqueCount +=1
            qqq-=1
    print("number of non-uniques hit (not displayed above, all of the above ARE unique): " + str(notUniqueCount))






if __name__ == "__main__":
    main()
