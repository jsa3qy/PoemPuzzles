from slide import *
from objectDefinitions import *
import sys
import numpy as np
from dataCleaningHelpers import *
from tilingHelpers import *
from objectDefinitions2 import *
import networkx as nx
from string import ascii_uppercase
from networkx.algorithms.approximation import clique_removal
from igraph import Graph
from igraph import *
from validity import *
import random

POEM_SIZE = 60
successCount = 0

def main():
    #file = open("syllablizedPoemOneSyllablePerWord.txt")
    file = open("piecesHex.txt")
    listOfLists = []
    for line in file:
        line = line.split(" , ")
        sublist = []
        for i in line:
            i = i.strip()
            sublist.append(i.split(" "))
        listOfLists.append(sublist)

    for orientation in listOfLists:
        for index, val in enumerate(orientation):
            for index2, val2 in enumerate(val):
                orientation[index][index2] = int(val2)
    ###listOfLists has all of the positions as a list[int] of indices

    tileObjectsInBuckets = []
    for sublist_orientations in listOfLists:
        tileObjects = []
        for orientation in sublist_orientations:
            goodToGo = True
            for i in orientation:
                if i >= POEM_SIZE:
                    goodToGo = False
            if goodToGo:
                tileObjects.append(tileObject(orientation))
        tileObjectsInBuckets.append(copy.deepcopy(tileObjects))

    for index,bucket in enumerate(tileObjectsInBuckets):
        newBucket = copy.deepcopy(bucket)
        for tile in newBucket:
            tempTile, good = slide(copy.deepcopy(tile), POEM_SIZE)
            tileObjectsInBuckets[index].append(tempTile)
            while good == 1:
                tempTile, good = slide(copy.deepcopy(tempTile), POEM_SIZE)
                tileObjectsInBuckets[index].append(tempTile)

    tileDescriptors = []
    tileDescriptorsInBuckets = []

    for index,bucket in enumerate(tileObjectsInBuckets):
        #make the tile descriptors into buckets too
        tileDescriptorsInBuckets.append([])
        for index2,thing in enumerate(bucket):
            tileDescriptors.append(tileDescriptor(thing.currentPosition, index, POEM_SIZE))
            tileDescriptorsInBuckets[index].append(tileDescriptor(thing.currentPosition, index, POEM_SIZE))


    #otherFile = open("howILoveThee.txt")
    otherFile = open("60SylPoem.txt")
    #otherFile = open("syllablizedPoemOneSyllablePerWord.txt")
    listOfSyls = readInSyllablePoem(otherFile)
    masterListOfSyllables = makeMasterListOfSyllables(listOfSyls)
    listOfSylNodes = makeSylNodes(listOfSyls)


    #in progress
    validListOfTileDescriptors = []
    validListOfTileDescriptorsInBuckets = []
    before = len(tileDescriptors)

    for index,node in enumerate(tileDescriptors):
        if valid(listOfSylNodes, node.rawTile):
            if node not in validListOfTileDescriptors:
                validListOfTileDescriptors.append(node)
        else:
            continue
    for index, bucket in enumerate(tileDescriptorsInBuckets):
        validListOfTileDescriptorsInBuckets.append([])
        for index2, node in enumerate(bucket):
            if valid(listOfSylNodes, node.rawTile):
                if node not in validListOfTileDescriptorsInBuckets[index]:
                    validListOfTileDescriptorsInBuckets[index].append(node)
            else:
                continue

#OK let's place three tiles
    validListOfTileDescriptorsInBuckets.sort(key=len)
    returnList = copy.deepcopy(validListOfTileDescriptorsInBuckets)

    length1 = len(validListOfTileDescriptorsInBuckets[0])
    length2 = len(validListOfTileDescriptorsInBuckets[1])
    length3 = len(validListOfTileDescriptorsInBuckets[2])
    solutionLength = 0
    tileSaved1 = None
    tileSaved2 = None
    tileSaved3 = None
    done = False
    iterationCount = 0
    for i1 in range(length1):
        for j1 in range(length2):
            for k1 in range(length3):
                if (iterationCount) < (length1*length2*length3/2):
                    iterationCount+=1
                    continue
                iterationCount+=1
                if solutionLength == 9:
                    done = True
                    break
                validListOfTileDescriptorsInBuckets = copy.deepcopy(returnList)
                tileSaved1 = copy.deepcopy(validListOfTileDescriptorsInBuckets[0][i1])
                tileSaved2 = copy.deepcopy(validListOfTileDescriptorsInBuckets[1][j1])
                tileSaved3 = copy.deepcopy(validListOfTileDescriptorsInBuckets[2][k1])
                if overlap(tileSaved1,tileSaved2) or overlap(tileSaved3,tileSaved1) or overlap(tileSaved3,tileSaved2):
                    continue
                del validListOfTileDescriptorsInBuckets[2]
                del validListOfTileDescriptorsInBuckets[1]
                del validListOfTileDescriptorsInBuckets[0]
                overlappedTiles = []
                for index,bucket in enumerate(validListOfTileDescriptorsInBuckets):
                    for i in bucket:
                        if overlap(i, tileSaved1):
                            overlappedTiles.append([index,i])
                        if overlap(i,tileSaved2):
                            overlappedTiles.append([index,i])
                        if overlap(i,tileSaved3):
                            overlappedTiles.append([index,i])
                for i in overlappedTiles:
                    try:
                        validListOfTileDescriptorsInBuckets[i[0]].remove(i[1])
                    except:
                        pass
                validListOfTileDescriptors = []
                for i in validListOfTileDescriptorsInBuckets:
                    validListOfTileDescriptors+=i

                print("iteration " + str(iterationCount) + " of " + str(length1*length2*length3))
                #random.shuffle(validListOfTileDescriptors)
                #validListOfTileDescriptors = validListOfTileDescriptors[0:len(validListOfTileDescriptors)]
                G = Graph()
                G.add_vertices(len(validListOfTileDescriptors))
                listOfEdgesToAdd = []
                for index1, node1 in enumerate(validListOfTileDescriptors):
                    for index2, node2 in enumerate(validListOfTileDescriptors):
                        if ((index2>index1) and not (overlap(node1, node2) or node1.bucketNum == node2.bucketNum)):
                            listOfEdgesToAdd.append((index1,index2))
                print("edges count: ", len(listOfEdgesToAdd))

                G.add_edges(listOfEdgesToAdd)
                print("made it")
                #solution = G.largest_cliques()
                solution = G.clique_number()
                print(solution)
                #solution = G.largest_independent_vertex_sets()
                #solution = G.independence_number()
                try:
                    solutionLength = solution
                    #solutionLength = len(solution[0])
                except:
                    print("solution pool length is " + str(len(solution)))

            if done:
                break


    print("we good boi")
    sys.exit(0)
    boardTile = np.empty(POEM_SIZE,  dtype='|S6')
    boardTile.flatten()
    for index, val in enumerate(boardTile):
        boardTile[index] = '3'
    letterIndex = 0
    try:
        solution1 = solution[0]
    except:
        print("no solution")
        sys.exit(0)

    for indexT, tileNum in enumerate(solution1):
        tile = validListOfTileDescriptors[tileNum]
        #tile.toString(1)
        for index in tile.rawTile:
            if index < POEM_SIZE:
                boardTile[index] = ascii_uppercase[letterIndex]
        letterIndex+=1
    for index in tileSaved1.rawTile:
        if index < POEM_SIZE:
            boardTile[index] = ascii_uppercase[letterIndex]
    letterIndex+=1
    for index in tileSaved2.rawTile:
        if index < POEM_SIZE:
            boardTile[index] = ascii_uppercase[letterIndex]
    letterIndex+=1
    for index in tileSaved3.rawTile:
        if index < POEM_SIZE:
            boardTile[index] = ascii_uppercase[letterIndex]
    letterIndex+=1


    boardTile = np.reshape(boardTile,(POEM_SIZE/10,10))
    print(boardTile)

def overlap(td1, td2):
    for i in td1.rawTile:
        if td2.binaryTile[i] == 1:
            return True
    return False

def placeTile(buckets, ones):

    if filled(ones):
        successCount+=1
        print(successCount)
        return True
    elif len(buckets) == 0:
        return False
    currentBucket = buckets[0]
    currentTile = currentBucket[0]
    for i in currentTile.currentPosition:
        if ones[i] == 0:
            del buckets[0][0]
            if len(buckets[0]) == 0:
                del buckets[0]
            onesCopy = copy.deepcopy(ones)
            success = placeTile(buckets, onesCopy)
            return success
    for i in currentTile.currentPosition:
        ones[i] = 0

    del buckets[0]
    onesCopyTwo = copy.deepcopy(ones)
    success2 = placeTile(buckets, onesCopyTwo)
    return success2


def filled(ones):
    for i in ones:
        if i == 1:
            return False
    successCount+=1
    return True



if __name__ == "__main__":
    main()
