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
import time


#12 pentominoes and 5 tetrominoes
#default is empty, will be appended to after user input
OMINOE_SIZE = []
#boolean values, 0s == no uniqueness, 1s == uniqueness
OMINOE_BOOLS = []
#default is 60, will be reassigned with user input
POEM_SIZE = 60
#iterations default is 1
iterations = 1

def main(inputList, poem, plainListOfSyllables):
    start = time.time()
    #OMINOE_SIZE2 == OMINOE_SIZE1 if you only want one type
    #format of inputFile is:
    #iterations poem_size number_of_ominoe_sizes ominoe_size_0 ... ominoe_size_n add_padding_boolean_0 ... add_padding_boolean_n
    user_specify = inputList

    try:
        TILINGS_TO_PRINT = int(user_specify[0])
        POEM_SIZE = int(user_specify[1])
        for i in range(int(user_specify[2])):
            OMINOE_SIZE.append(int(user_specify[3+i]))
            OMINOE_BOOLS.append(int(user_specify[3+int(user_specify[2])+i]))
    except:
        print("ERROR")
        sys.exit(1)

    #error checking
    if 6 in OMINOE_SIZE and OMINOE_BOOLS[OMINOE_SIZE.index(6)] == 1:
        print("ERROR")
        sys.exit(1)

    bucketsHashMap = {}
    #myFile = open("poem.txt")
    #otherFile = open("howILoveThee.txt")
    #otherFile = open("syllablizedPoemOneSyllablePerWord.txt")
    #otherFile = open("syllablizedPoem.txt")

    #No punctuation in words!
    #listOfWords = readInRawPoem(myFile)
    listOfSyls = plainListOfSyllables #readInSyllablePoem(otherFile)
    masterListOfSyllables = makeMasterListOfSyllables(listOfSyls)
    listOfSylNodes = makeSylNodes(poem) #makeSylNodes(listOfSyls)

    for index, j in enumerate(OMINOE_SIZE):
        for i, node in enumerate(listOfSylNodes):
            myOminoe = ominoe(j)
            myOminoe.reachableIndices+= listOfReachableIndices(i, POEM_SIZE)
            extendOminoe(myOminoe, i, listOfSylNodes)
            expandInAllDirections(myOminoe, listOfSylNodes)

    #let's take valid tiles from the ominoe objects and sort them
    sortedListOfTiles = []
    for validTile in listOfTiles:
        sortedListOfTiles.append(validTile.getIndicesInOminoe())
    builtListOfSimpleOminoes = buildSimpleOminoes(sortedListOfTiles)
    placeIntoBuckets(builtListOfSimpleOminoes)

    print("Number of tiles constructed: " + str(len(sortedListOfTiles)))
    placeIntoBuckets(builtListOfSimpleOminoes)
    print("number of different ominoe shapes:",len(buckets))

    validCount = 0
    sortedListOfTilesCopy = copy.deepcopy(sortedListOfTiles)
    notUniqueCount = 0

    for qqq in range(TILINGS_TO_PRINT):
        cover = []
        numPadding = len(buckets)
        if qqq == 0:
            sortedListOfTiles = []
            bucketAddition = POEM_SIZE
            for i,bucket in enumerate(buckets):
                if len(buckets[i][0].tile) in OMINOE_SIZE:
                    if OMINOE_BOOLS[OMINOE_SIZE.index(len(buckets[i][0].tile))] == 1:
                        for ominoeObject in bucket:
                            tempTile = ominoeObject.tile
                            tempTile.append(bucketAddition)
                            sortedListOfTiles.append(tempTile)
                        bucketAddition +=1
                    else:
                        for ominoeObject in bucket:
                            sortedListOfTiles.append(ominoeObject.tile)
            rangeIncrease = bucketAddition-POEM_SIZE

        random.shuffle(sortedListOfTiles)
        true = 0
        listOfUsableInputs = []
        for tile in sortedListOfTiles:
            referenceTile = np.zeros(POEM_SIZE+rangeIncrease)
            for index in tile:
                referenceTile[index] += 1
            listOfUsableInputs.append(referenceTile)
####################################################################
        S = np.array(listOfUsableInputs, dtype='int32')
        end = time.time()
        print("time to finish pre-process: "+str(end - start))
        start = time.time()
        cover = ec.get_exact_cover(S)
        end = time.time()
        print("number of tiles: "+str(len(listOfUsableInputs)))
        print("time to finish exact cover: "+str(end - start))
####################################################################
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
            else:
                print("invalid tiling")
                #sys.exit(1)

            finalListToDisplay = []
            boardTile = np.empty(POEM_SIZE,  dtype='|S6')
            boardTile.flatten()
            for index, val in enumerate(boardTile):
                boardTile[index] = ''
            letterIndex = 0
            return finalList

            for indexT, tile in enumerate(finalList):
                for index in tile:
                    if index < POEM_SIZE:
                        boardTile[index] = ascii_uppercase[letterIndex]
                letterIndex+=1

            boardTile = np.reshape(boardTile,(POEM_SIZE/10,10))
            print("iteration " + str(qqq) + ": ")
            print(boardTile)
        else:
            notUniqueCount +=1
            qqq-=1
    print("number of non-uniques hit (not displayed above, all of the above ARE unique): " + str(notUniqueCount))

#if __name__ == "__main__":
    #solution = main(["1", "60", "1", "5", "0"])
    #print(solution)
