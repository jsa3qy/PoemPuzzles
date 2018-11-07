from dataCleaningHelpers import *
from tilingHelpers import *
from objectDefinitions import *

def main():
    myFile = open("poem.txt")
    otherFile = open("syllablizedPoem.txt")

    #No punctuation in words!
    listOfWords = readInRawPoem(myFile)
    listOfSyls = readInSyllablePoem(otherFile)
    masterListOfSyllables = makeMasterListOfSyllables(listOfSyls)
    listOfSylNodes = makeSylNodes(listOfSyls)
    for i, node in enumerate(listOfSylNodes):
        node.toString()




if __name__ == "__main__":
    main()
