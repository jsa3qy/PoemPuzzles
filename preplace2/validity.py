def valid(sylNodes, tile):
    tile.sort()
    for i in tile:
        curNode = sylNodes[i]
        for i in range(curNode.sylLeft):
            if curNode.absolutePos - i - 1 not in tile:
                return False
        for i in range(curNode.sylRight):
            if curNode.absolutePos + i + 1 not in tile:
                return False
    return True
