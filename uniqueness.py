
uniquenessMap = {}

def uniqueCover(cover):
    cover.sort()
    hashString = ""
    for tile in cover:
        for item in tile:
            hashString += str(item)+"-"
    if uniquenessMap.get(hashString) != None:

        return False
    else:
        uniquenessMap[hashString] = 1
        return True
