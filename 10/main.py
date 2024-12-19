def partOne():
    # Generate all directions into tuples
    dd = generateDirections()
    
    result = 0
    for i in range(row):
        for j in range(col):
            r = checkRoute(int(lines[i][j]), (i, j), 0, [], dd)
            result += len(r)

    return result


def checkRoute(currElevation, currPos, nextElevation, visited, dd):
    if (currElevation != nextElevation):
        return visited

    if (nextElevation == 9 and currElevation == 9):
        if not (currPos in visited):
            visited.append(currPos)
        return visited

    resultList = []
    for d in dd:
        nextPos = list(currPos)
        nextPos[0] += d[0] 
        nextPos[1] += d[1]
        nextPos = tuple(nextPos)
        if not (0 <= nextPos[0] < row and 0 <= nextPos[1] < col):
            continue

        newVisited = checkRoute(int(lines[nextPos[0]][nextPos[1]]), 
                                nextPos, 
                                nextElevation + 1, 
                                visited, 
                                dd)
        for v in newVisited:
            if not (v in resultList):
                resultList.append(v)

    return resultList




def generateDirections():
    dd = []
    # Up, Right, Down, Left
    dd.append((0, -1))
    dd.append((1, 0))
    dd.append((0, 1))
    dd.append((-1, 0))
    return dd


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.read().strip().split("\n")
    row = len(lines)
    col = len(lines[0])

    print(partOne())
