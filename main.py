from dataCleaningHelpers import *
from tilingHelpers import *
from objectDefinitions import *
from test import *
from setCover import *
import numpy as np
import random
import exact_cover_np as ec

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
        myOminoe = ominoe(5)
        myOminoe.reachableIndices+= listOfReachableIndices(i, 60)
        extendOminoe(myOminoe, i, listOfSylNodes)
        expandInAllDirections(myOminoe, listOfSylNodes)

    #let's take valid tiles from the ominoe objects and sort them
    sortedListOfTiles = []
    for validTile in listOfTiles:
        sortedListOfTiles.append(validTile.getIndicesInOminoe())
    validCount =0
    for i in range(10):
        sortedListOfTiles.sort(key=lambda x: x[0])
        random.shuffle(sortedListOfTiles)
        true = 0
        #print("Done with tile enumeration, finding a valid tiling!")
        simpleOminoes = []
        for i in sortedListOfTiles:
            tempString = ""
            for val in i:
                tempString+=str(val)
            simpleOminoes.append(simpleOminoe(tempString,i))
        universeList = []
        for i in range(60):
            universeList.append(i)


        #random.shuffle(simpleOminoes)
        listOfUsableInputs = []
        for tile in simpleOminoes:
            referenceTile = np.zeros(60)
            for index in tile.listOfIndices:
                referenceTile[index] += 1
            listOfUsableInputs.append(referenceTile)
        S = np.array(listOfUsableInputs, dtype='int32')

        cover = ec.get_exact_cover(S)

        finalList = []
        for i in cover:
            finalList.append(sortedListOfTiles[i])

        check = np.zeros(60)
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
    for tile in finalList:
        boardTile = np.empty(60,  dtype='|S6')
        boardTile.flatten()
        for i in range(60):
            boardTile[i] = "."
        for index in tile:
            boardTile[index] = "X"#masterListOfSyllables[index]

        boardTile = np.reshape(boardTile,(6,10))
        print(boardTile)
            #print("The solution is a valid solution")

            #print("The solution is invalid, something must have gone wrong")
        #simpleOminoes.pop(cover[0])'''


if __name__ == "__main__":
    main()
