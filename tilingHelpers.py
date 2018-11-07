def makeSylNodes(listOfSyls, listOfSylsNoWords):
    listOfSylNodes = []
    for numWord, word in enumerate(listOfSyls):
        for i, syl in enumerate(word):
            listOfSylNodes.append(sylNode(word, i, str(numWord)+"-"+str(i), listOfSylsNoWords.index(syl)))
    return listOfSylNodes

def makeMasterListOfSyllables(listOfSyls):
    masterListOfSyls = []
    for numWord, word in enumerate(listOfSyls):
        for i, syl in enumerate(word):
            masterListOfSyls.append(syl)
    return masterListOfSyls

def listOfReachableIndices(index, listOfSylsSize):
    #index is index in whole poem, that is, the #syllable
    reachable = []
    if index>0:
        reachable.append(index-1)
    if index<listOfSylsSize-1:
        reachable.append(index+1)
    if index + 10 < listOfSylsSize:
        reachable.append(index+10)
    if index >= 10:
        reachable.append(index-10)
    return reachable

def extendOminoe(curOminoe, index, listofSylNodes):
    maybeNode = listOfSylNodes[index]
    if curOminoe.sylAvailable >= maybeNode.wordSize:
        curOminoe.sylList.append(maybeNode)
        curOminoe.extendReachables(index)
        for node in range(1,maybeNode.sylLeft+1):
            curOminoe.sylList.append(listOfSylNodes[index - node])
            curOminoe.extendReachables(index-node)
        for node in range(1,maybeNode.sylRight+1):
            curOminoe.sylList.append(listOfSylNodes[index+node])
            curOminoe.extendReachables(index+node)
