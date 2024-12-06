def partOne():
    f = open("input.txt", "r")
    result = 0

    # Create 2 lists
    listX = []
    listY = []
    for line in f:
        list = line.split("   ")
        x = int(list[0])
        y = int(list[1])

        listX.append(x)
        listY.append(y)

    # Sort both lists
    listX.sort()
    listY.sort()

    # Calculate total distance
    for i in range(len(listX)):
        x = listX[i]
        y = listY[i]
        result += abs(x - y)

    return result

def partTwo():
    f = open("input.txt", "r")
    result = 0

    # Create 2 lists
    listX = []
    listY = []
    for line in f:
        list = line.split("   ")
        x = int(list[0])
        y = int(list[1])

        listX.append(x)
        listY.append(y)

    # Naive O(n^2) solution
    for x in listX:
        for y in listY:
            if (x == y):
                result += x

    return result

if __name__ == '__main__':
    print(partOne())
    print(partTwo())

