from dataCleaningHelpers import *
from objectDefinitions import *


def main():
    myFile = open("poem.txt")
    otherFile = open("syllablizedPoem.txt")

    #No punctuation in words!
    listOfWords = readInRawPoem(myFile)
    listOfSyls = readInSyllablePoem(otherFile)
    listOfSylNodes = []
    for numWord, word in enumerate(listOfSyls):
        for i, syl in enumerate(word):
            listOfSylNodes.append(sylNode(word, i, str(numWord)+"-"+str(i)))
    for node in listOfSylNodes:
        print(node.toString())


if __name__ == "__main__":
    main()
