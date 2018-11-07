from objectDefinitions import *
from string import punctuation
from hyphen import *
from hyphen.dictools import *

def readInRawPoem(myFile):
    listOfWords = []
    for line in myFile:
        listOfWords+=line.split()

    for i, word in enumerate(listOfWords):
        #https://www.quora.com/How-do-I-remove-punctuation-from-a-Python-string
        listOfWords[i] = ''.join(c for c in word if c not in punctuation)

    return listOfWords

def returnListOfSyllables(listOfWords):
    h_en = Hyphenator('en_US')
    listOfSyls = []
    for i, word in enumerate(listOfWords):
        temp = h_en.syllables(word)
        if temp != []:
            listOfSyls.append(h_en.syllables(word))
        else:
            listOfSyls.append([word])
    for i in listOfSyls:
        print(i)

    return listOfSyls

def readInSyllablePoem(myFile):
    listOfSyls = []
    for line in myFile:
        line = line.split()
        listOfSyls.append(line)
    return listOfSyls
