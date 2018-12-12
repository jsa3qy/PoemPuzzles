from objectDefinitions import *
from string import punctuation
from hyphen import *

#returns a list of the words
def readInRawPoem(myFile):
    listOfWords = []
    for line in myFile:
        listOfWords+=line.split()

    for i, word in enumerate(listOfWords):
        #https://www.quora.com/How-do-I-remove-punctuation-from-a-Python-string
        listOfWords[i] = ''.join(c for c in word if c not in punctuation)

    return listOfWords

#takes in a list of words and returns the syllables
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

#For when the poem is already split into syllables
def readInSyllablePoem(myFile):
    listOfSyls = []
    for line in myFile:
        line = line.split()
        listOfSyls.append(line)
    return listOfSyls
