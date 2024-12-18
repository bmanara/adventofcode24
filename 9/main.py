def partOne():
    line = ""
    xs = []
    with open("input.txt") as f:
        line = f.readline().strip()

    for i in range(len(line)):
        x = int(line[i])

        if not (i % 2 == 0):
            for j in range(x):
                xs.append(".")
        else:
            for j in range(x):
                xs.append(int(i / 2))

    start = 0
    end = len(xs) - 1

    while (start < end):
        if (xs[start] == "."):
            xs[end], xs[start] = xs[start], xs[end]

        start += 1
        while (xs[end] == "."):
            end -= 1


    result = 0
    i = 1
    while (xs[i] != "."):
        result += i * xs[i]
        i += 1

    return result

if __name__ == '__main__':
    print(partOne())
