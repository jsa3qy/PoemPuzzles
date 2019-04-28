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
    #file = open("pieces.txt")
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
    #validListOfTileDescriptorsInBuckets.reverse()

    print('')
    for i in validListOfTileDescriptorsInBuckets:
        print(len(i))
    sys.exit(0)
    random.shuffle(validListOfTileDescriptorsInBuckets[0])
    tileSaved1 = copy.deepcopy(validListOfTileDescriptorsInBuckets[0][0])
    del validListOfTileDescriptorsInBuckets[0]
    overlappedTiles = []
    for index,bucket in enumerate(validListOfTileDescriptorsInBuckets):
        for i in bucket:
            if overlap(i, tileSaved1):
                overlappedTiles.append([index,i])
    for i in overlappedTiles:
        validListOfTileDescriptorsInBuckets[i[0]].remove(i[1])
    random.shuffle(validListOfTileDescriptorsInBuckets[1])
    tileSaved2 = copy.deepcopy(validListOfTileDescriptorsInBuckets[1][0])
    del validListOfTileDescriptorsInBuckets[1]
    overlappedTiles = []
    for index,bucket in enumerate(validListOfTileDescriptorsInBuckets):
        for i in bucket:
            if overlap(i, tileSaved2):
                overlappedTiles.append([index,i])
    for i in overlappedTiles:
        validListOfTileDescriptorsInBuckets[i[0]].remove(i[1])
    random.shuffle(validListOfTileDescriptorsInBuckets[2])
    tileSaved3 = copy.deepcopy(validListOfTileDescriptorsInBuckets[2][0])
    del validListOfTileDescriptorsInBuckets[2]
    # overlappedTiles = []
    # for index,bucket in enumerate(validListOfTileDescriptorsInBuckets):
    #     for i in bucket:
    #         if overlap(i, tileSaved3):
    #             overlappedTiles.append([index,i])
    # for i in overlappedTiles:
    #     validListOfTileDescriptorsInBuckets[i[0]].remove(i[1])
    # print('')
    # for i in validListOfTileDescriptorsInBuckets:
    #     print(len(i))

    validListOfTileDescriptors = []
    for i in validListOfTileDescriptorsInBuckets:
        validListOfTileDescriptors+=i


    #AHHHHH
    print("Tiles before pruning: ",before)
    print("number of tiles: ",len(validListOfTileDescriptors))
    random.shuffle(validListOfTileDescriptors)
    validListOfTileDescriptors = validListOfTileDescriptors[0:len(validListOfTileDescriptors)/8]
    print("Tiles before pruning: ",before)
    print("number of tiles: ",len(validListOfTileDescriptors))
    #G=nx.Graph()
    G = Graph()
    G.add_vertices(len(validListOfTileDescriptors))

    listOfEdgesToAdd = []
    for index1, node1 in enumerate(validListOfTileDescriptors):
        for index2, node2 in enumerate(validListOfTileDescriptors):
            if ((index2>index1) and not (overlap(node1, node2) or node1.bucketNum == node2.bucketNum)):
                listOfEdgesToAdd.append((index1,index2))

    #for i in listOfEdgesToAdd:
        #print(validListOfTileDescriptors[i[0]].rawTile)
        #print(validListOfTileDescriptors[i[0]].bucketNum)
        #print(validListOfTileDescriptors[i[1]].rawTile)
        #print(validListOfTileDescriptors[i[1]].bucketNum)
        #print('')


    print("edges count: ", len(listOfEdgesToAdd))
    G.add_edges(listOfEdgesToAdd)
    print("made it")
    solution = G.largest_cliques()
    #solution = G.clique_number()
    #solution = G.largest_independent_vertex_sets()
    #solution = G.independence_number()
    print("list of solutions: ")
    print(solution)



    boardTile = np.empty(POEM_SIZE,  dtype='|S6')
    boardTile.flatten()
    for index, val in enumerate(boardTile):
        boardTile[index] = '3'
    letterIndex = 0
    if len(solution) == 0:
        print("no solution")
        sys.exit(0)
    solution1 = solution[0]
    #print(solution1)
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
    # for index in tileSaved3.rawTile:
    #     if index < POEM_SIZE:
    #         boardTile[index] = ascii_uppercase[letterIndex]
    # letterIndex+=1

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
