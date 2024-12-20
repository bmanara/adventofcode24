import time


def partOne():
    # Blink 25 times
    for i in range(25):
        # Loop through all numbers
        size = len(numbers)
        j = 0

        while (j < size):
            n = numbers[j]
            if (n == 0): # Rule 1
                numbers[j] = 1

            elif (len(str(n)) % 2 == 0): # Rule 2
                stringN = str(n)
                half = int(len(stringN) / 2)
                first = int(stringN[0:half])
                second = int(stringN[half:len(stringN)])
                numbers[j] = first
                numbers.insert(j + 1, second)

                size += 1
                j += 1

            else: # Rule 3
                numbers[j] = numbers[j] * 2024
            j += 1

    return len(numbers)




if __name__ == '__main__':
    start_time = time.time()
    numbers = []
    with open("input.txt") as f:
        numbers = [int(n) for n in f.read().strip().split(" ")]

    print(partOne())
    print("Runtime: %s seconds" % (time.time() - start_time))
