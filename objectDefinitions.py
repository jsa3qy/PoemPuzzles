class sylNode:
    #constructor 1
    def __init__(self, wordSize, sylRight, sylLeft, tag):
        self.wordSize = wordSize
        self.sylRight = sylRight
        self.sylLeft = sylLeft
        self.tag = tag

    #constructor 2
    def __init__(self, listOfSyls, index, tag):
        self.wordSize = len(listOfSyls)
        self.sylRight = self.wordSize - index + 1
        self.sylLeft = index
        self.tag = tag

class ominoe:
    #constructor
    def __init__(self, size):
        self.sylAvailable = size
        self.size = size
        self.sylList = []
