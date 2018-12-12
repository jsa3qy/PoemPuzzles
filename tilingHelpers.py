from objectDefinitions import *
import copy
import sys
from test import testForValidity

listOfTiles = []
alreadyCounted = {}

def makeSylNodes(listOfSyls):
    listOfSylNodes = []
    for numWord, word in enumerate(listOfSyls):
        for i, syl in enumerate(word):
            tempNode = sylNode(word, i, str(numWord)+str(i), len(listOfSylNodes))
            listOfSylNodes.append(tempNode)
    return listOfSylNodes

def makeMasterListOfSyllables(listOfSyls):
    masterListOfSyls = []
    for numWord, word in enumerate(listOfSyls):
        for i, syl in enumerate(word):
            masterListOfSyls.append(syl)
    return masterListOfSyls

def extendOminoe(curOminoe, index, listOfSylNodes):
    maybeNode = listOfSylNodes[index]
    #so I an check before verses after for debugging
    copyOfOminoe = copy.deepcopy(curOminoe)
    if curOminoe.sylAvailable >= maybeNode.wordSize:
        curOminoe.sylList.append(listOfSylNodes[index])
        curOminoe.removeReachables(index)
        curOminoe.extendReachables(index)
        if (maybeNode.sylLeft > 0):
            for node in range(1,maybeNode.sylLeft+1):
                curOminoe.sylList.append(listOfSylNodes[index - node])
                curOminoe.removeReachables(index-node)
                curOminoe.extendReachables(index-node)
        if (maybeNode.sylRight > 0):
            for node in range(1,maybeNode.sylRight+1):
                curOminoe.sylList.append(listOfSylNodes[index+node])
                curOminoe.removeReachables(index+node)
                curOminoe.extendReachables(index+node)
        curOminoe.sylAvailable -= maybeNode.wordSize
    else:
        curOminoe.removeReachables(index)
        for node in range(1,maybeNode.sylLeft+1):
            if (node-index) in curOminoe.reachableIndices:
                curOminoe.removeReachables(index-node)
        for node in range(1,maybeNode.sylRight+1):
            if (node+index) in curOminoe.reachableIndices:
                curOminoe.removeReachables(index+node)


    if (copyOfOminoe.sylAvailable < 5 and (testForValidity(curOminoe.getIndicesInOminoe()) == False) and (testForValidity(copyOfOminoe.getIndicesInOminoe()))):
        print("reachables: ")
        print(copyOfOminoe.reachableIndices)
        print(copyOfOminoe.getIndicesInOminoe())
        print("\n")
        print(curOminoe.getIndicesInOminoe())
        print("\n")
        print("done")
        if (len(copyOfOminoe.sylList) > 4):
            sys.exit(0)
    return curOminoe

def expandInAllDirections(ominoe, listOfSylNodes):
    global listOfTiles
    global alreadyCounted
    #don't need this?

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
