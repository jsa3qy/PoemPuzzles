from objectDefinitions import *

listOfTiles = []
alreadyCounted = {}

def makeSylNodes(listOfSyls):
    listOfSylNodes = []
    for numWord, word in enumerate(listOfSyls):
        for i, syl in enumerate(word):
            tempNode = sylNode(word, i, str(numWord)+"-"+str(i), len(listOfSylNodes))
            listOfSylNodes.append(tempNode)
    return listOfSylNodes

def makeMasterListOfSyllables(listOfSyls):
    masterListOfSyls = []
    for numWord, word in enumerate(listOfSyls):
        for i, syl in enumerate(word):
            masterListOfSyls.append(syl)
    return masterListOfSyls

def extendOminoe(curOminoe, index, listofSylNodes):
    maybeNode = listOfSylNodes[index]
    if curOminoe.sylAvailable >= maybeNode.wordSize:
        curOminoe.sylList.append(maybeNode)
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
    return curOminoe


#def expandInAllDirections(ominoe, listofSylNodes):
    #global listOfTiles
    #for index in ominoe.reachableIndices:
        #tempOminoe = extendOminoe(ominoe, index, listOfSylNodes)
        #if
