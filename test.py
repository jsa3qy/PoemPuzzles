from objectDefinitions import *
import copy

def testForValidity(ListOfValsInOminoe):
        if len(ListOfValsInOminoe) == 1:
            return True
        tempOminoe = copy.deepcopy(ListOfValsInOminoe)
        firstSpot = tempOminoe[0]
        del tempOminoe[0]
        reachableIndices = []
        for otherItem in tempOminoe:
            reachableIndices+=listOfReachableIndices(otherItem, 60)
        if firstSpot in reachableIndices:
            return testForValidity(tempOminoe)
        else:
            return False

def testForValidity2(ListOfValsInOminoe):
    tempOminoe = copy.deepcopy(ListOfValsInOminoe)
    for i, obj in enumerate(tempOminoe):
        tempOminoe[i] = [obj,listOfReachableIndices(obj, 60)]
    count = 0
    for obj in tempOminoe:
        for obj2 in tempOminoe:
            if obj[0] == obj2[0]:
                continue
            elif obj[0] in obj2[1]:
                count+=1
    if count >= 8:
        return True
    else:
        return False
