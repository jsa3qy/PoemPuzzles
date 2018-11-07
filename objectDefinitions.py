class sylNode:
    #constructor 1
    def __init__(self, syl, wordSize, sylRight, sylLeft, tag):
        self.wordSize = wordSize
        self.sylRight = sylRight
        self.sylLeft = sylLeft
        self.tag = tag
        self.syl = syl

    #constructor 2
    def __init__(self, listOfSyls, index, tag):
        self.wordSize = len(listOfSyls)
        self.sylRight = self.wordSize - index - 1
        self.sylLeft = index
        self.tag = tag
        self.syl = listOfSyls[index]

    def toString(self):
        print("word size: " + str(self.wordSize) + "\nsylRight: " + str(self.sylRight) + "\nsylLeft: " + str(self.sylLeft) + "\ntag: " + str(self.tag) + "\nsyl: " + str(self.syl))

class ominoe:
    #constructor
    def __init__(self, size):
        self.sylAvailable = size
        self.size = size
        self.sylList = []
