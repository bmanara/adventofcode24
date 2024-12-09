def partOne():
    x = 0
    y = 0

    # Find starting position
    for i in range(row):
        for j in range(col):
            if (lines[i][j] == "^"):
                x = i
                y = j

    
    # Up, Right, Down, Left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Traverse until we reach out of bounds
    currentDirection = 0
    visited = 0

    while (0 <= x < row and 0 <= y < col):
        if (lines[x][y] == "."):
            visited += 1
            lines[x][y] = "X"

        dx = directions[currentDirection][0]
        dy = directions[currentDirection][1]
        
        # Check if there is obstacle
        x_next = x + dx
        y_next = y + dy
        
        if (x_next < 0 or x_next >= row or y_next < 0 or y_next >= col):
            break

        print(lines[x_next][y_next])
        if (lines[x_next][y_next] == "#"):
            currentDirection = (currentDirection + 1) % 4
            dx = directions[currentDirection][0]
            dy = directions[currentDirection][1]

        x += dx
        y += dy

    return visited + 1

if __name__ == '__main__':
    # Read input and put into array
    with open("input.txt") as f:
        lines = f.read().strip().split("\n")
        row = len(lines)
        col = len(lines[0])

    for k in range(row):
        lines[k] = [char for char in lines[k]]

    print(partOne())
