import copy
import sys
from test import *
from objectDefinitions2 import *
from main import POEM_SIZE

listOfTiles = []
alreadyCounted = {}

#build the list of node objects
def makeSylNodes(listOfSyls):
    listOfSylNodes = []
    for numWord, word in enumerate(listOfSyls):
        for i, syl in enumerate(word):
            tempNode = sylNode(word, i, str(numWord)+str(i), len(listOfSylNodes))
            listOfSylNodes.append(tempNode)
    return listOfSylNodes

#build a master list of syllables with absolute position
def makeMasterListOfSyllables(listOfSyls):
    masterListOfSyls = []
    for numWord, word in enumerate(listOfSyls):
        for i, syl in enumerate(word):
            masterListOfSyls.append(syl)
    return masterListOfSyls

#will add an index and the rest of the word that index is a part of to the ominoe if possible
#also takes care of reachable indices as a result
def extendOminoe(curOminoe, index, listOfSylNodes):
    left = False
    right = False
    maybeNode = listOfSylNodes[index]
    #so I an check before verses after for debugging
    copyOfOminoe = copy.deepcopy(curOminoe)

    if curOminoe.sylAvailable >= maybeNode.wordSize:
        curOminoe.sylList.append(listOfSylNodes[index])
        curOminoe.removeReachables(index)
        curOminoe.extendReachables(index, POEM_SIZE)
        '''if somethingWrongHere(curOminoe):
            print("main")
            print(curOminoe.reachableIndices)
            print(curOminoe.getIndicesInOminoe())
            print("just added: " + str(listOfSylNodes[index].absolutePos))
            print("reachables before: ")
            print(copyOfOminoe.reachableIndices)

            print("\n")'''
        if (maybeNode.sylLeft > 0):
            for node in range(1,maybeNode.sylLeft+1):
                left = True
                curOminoe.sylList.append(listOfSylNodes[index - node])
                curOminoe.removeReachables(index-node)
                curOminoe.extendReachables(index-node, POEM_SIZE)
        if (maybeNode.sylRight > 0):
            for node in range(1,maybeNode.sylRight+1):
                right = True
                curOminoe.sylList.append(listOfSylNodes[index+node])
                curOminoe.removeReachables(index+node)
                curOminoe.extendReachables(index+node, POEM_SIZE)
        curOminoe.sylAvailable -= maybeNode.wordSize
    else:
        curOminoe.removeReachables(index)
        for node in range(1,maybeNode.sylLeft+1):
            if (node-index) in curOminoe.reachableIndices:
                curOminoe.removeReachables(index-node)
        for node in range(1,maybeNode.sylRight+1):
            if (node+index) in curOminoe.reachableIndices:
                curOminoe.removeReachables(index+node)
    return curOminoe

#recursive function, will go through all indices and try to expand the ominoe to those indices.
#calls itself on the original passed in ominoe as well as the new ominoe with an added index to it.
def expandInAllDirections(ominoe, listOfSylNodes):
    global listOfTiles
    global alreadyCounted
    tempOminoe = copy.deepcopy(ominoe)
    indexNum = 0
    while (indexNum < len(tempOminoe.reachableIndices)):
        index = tempOminoe.reachableIndices[indexNum]
        if (tempOminoe.sylAvailable > 0):
            tempOminoe = extendOminoe(tempOminoe, index, listOfSylNodes)
        if tempOminoe.sylAvailable == 0:
            if alreadyCounted.get(tempOminoe.stringToHash()) == None:
                alreadyCounted[tempOminoe.stringToHash()] = 1
                listOfTiles.append(tempOminoe)
                return
        if (tempOminoe.sylAvailable > 0):
            expandInAllDirections(tempOminoe, listOfSylNodes)
        if index in ominoe.reachableIndices:
            if (ominoe.sylAvailable > 0):
                ominoe.removeReachables(index)
        if (ominoe.sylAvailable > 0) and (len(ominoe.reachableIndices) > 0):
            expandInAllDirections(ominoe, listOfSylNodes)
        indexNum+=1
    return
