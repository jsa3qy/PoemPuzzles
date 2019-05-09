from objectDefinitions import *
import copy
#slide right until can't slide right anymore, then push down a row and bring all the way back to the left
def slide(tile, POEM_SIZE):
    canMoveRight = True
    canMoveDown = True
    for index in tile.currentPosition:
        if (index+1)%10 == 0:
            canMoveRight = False
        if (index+10 >= POEM_SIZE):
            canMoveDown = False
        if index >= POEM_SIZE:
            return tile, -2

    if (not canMoveRight) and (not canMoveDown):
        return tile, -1
    if (not canMoveRight) and canMoveDown:
        tile.currentPosition = copy.deepcopy(tile.leftMostPosition)
        for index, val in enumerate(tile.leftMostPosition):
            tile.currentPosition[index] = val+10
        tile.leftMostPosition = copy.deepcopy(tile.currentPosition)

        return tile, 1
    if canMoveRight:
        for index, val in enumerate(tile.currentPosition):
            tile.currentPosition[index] = val+1

        return tile, 1
