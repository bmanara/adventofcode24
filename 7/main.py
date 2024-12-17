def partOne():
    xs = []
    with open("input.txt") as f:
        i = 0
        for line in f:
            xs.append(line.split(": "))
            xs[i][0] = int(xs[i][0])
            xs[i][1] = [int(x) for x in xs[i][1].split(" ")]
            i += 1
    

    result = 0
    # Naive solution, try all possible substructures
    # However, we should be able to "narrow it down", if we exceed, do not bother exploring further.
    for x in xs:
        goal = x[0]
        numerals = x[1]
        r = attempt(0, 0, numerals, goal)
        if r != -1:
            result += r
        
    return result
        

def attempt(idx, curr, numerals, goal):
    if (idx == len(numerals) and curr == goal):
        return curr
    elif (idx == len(numerals) and curr != goal):
        return -1
    
    if (curr > goal):
        return -1

    sum = attempt(idx + 1, add(curr, numerals[idx]), numerals, goal)
    product = attempt(idx + 1, multiply(curr, numerals[idx]), numerals, goal)

    return product if sum == -1 else sum 


# Define recursion here. Might be better to write recursion down with substructures

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

if __name__ == '__main__':
    print(partOne())
