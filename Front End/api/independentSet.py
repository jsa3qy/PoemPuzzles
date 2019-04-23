from dataCleaningHelpers import *
from tilingHelpers import *
from objectDefinitions import *
from test import *
from setCover import *
import numpy as np
import random
import exact_cover_np as ec
from buckets import *
import sys
from string import ascii_uppercase
from uniqueness import uniqueCover

OMINOE_SIZE = [4, 5]
POEM_SIZE = 80
TILINGS_TO_PRINT = 10

def main():
    otherFile = open("howILoveThee.txt")
    #otherFile = open("syllablizedPoemOneSyllablePerWord.txt")
    #otherFile = open("syllablizedPoem.txt")
    #No punctuation in words!
    #listOfWords = readInRawPoem(myFile)
    listOfSyls = readInSyllablePoem(otherFile)
    masterListOfSyllables = makeMasterListOfSyllables(listOfSyls)

    listOfSylNodes = makeSylNodes(listOfSyls)
    for i in listOfSylNodes:
        i.toString()

    


if __name__ == "__main__":
    main()
