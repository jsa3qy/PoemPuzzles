from objectDefinitions import *

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
    if curOminoe.sylAvailable >= maybeNode.wordSize:
        curOminoe.sylList.append(listOfSylNodes[index])
        curOminoe.extendReachables(index)
        curOminoe.removeReachables(index)
        for node in range(1,maybeNode.sylLeft+1):
            curOminoe.sylList.append(listOfSylNodes[index - node])
            curOminoe.extendReachables(index-node)
            curOminoe.removeReachables(index-node)
        for node in range(1,maybeNode.sylRight+1):
            curOminoe.sylList.append(listOfSylNodes[index+node])
            curOminoe.extendReachables(index+node)
            curOminoe.removeReachables(index+node)
        curOminoe.sylAvailable -= maybeNode.wordSize
    else:
        curOminoe.valid = False
    return curOminoe

def expandInAllDirections(ominoe, listOfSylNodes):
    global listOfTiles
    global alreadyCounted
    tempList = ominoe.reachableIndices
    tempOminoe = ominoe
    for index in tempList:
        if index not in ominoe.reachableIndices:
            continue
        tempOminoe = extendOminoe(tempOminoe, index, listOfSylNodes)
        if tempOminoe.sylAvailable == 0:
            if alreadyCounted.get(tempOminoe.stringToHash()) != None:
                continue
            else:
                alreadyCounted[tempOminoe.stringToHash()] = 1
                listOfTiles.append(tempOminoe)

        elif tempOminoe.valid == False:
            tempOminoe.valid = True
            tempOminoe.removeReachables(index)
        expandInAllDirections(tempOminoe, listOfSylNodes)
