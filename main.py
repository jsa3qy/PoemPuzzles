from helpers import *
from objectDefinitions import *


def main():
    myFile = open("poem.txt")

    #No punctuation in words!
    listOfWords = readInRawPoem(myFile)

    listOfSyls = returnListOfSyllables(listOfWords)
    print(listOfSyls)

if __name__ == "__main__":
    main()
