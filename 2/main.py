def partOne():
	f = open("input.txt", "r")
	result = 0

	isIncreasing = False

	# Loop through all reports
	for report in f:
		levels = [int(x) for x in report.split(" ")]
		first = levels[0]
		second = levels[1]

		# Check if levels are increasing or decreasing
		if (first > second):
			isIncreasing = False 
		elif (first < second):
			isIncreasing = True 
		else:
			continue

		# Loop through rest of levels
		isCorrect = True
		for i in range(0, len(levels) - 1):
			check = levels[i + 1] - levels[i]
			if (isIncreasing):
				if (check <= 0 or check > 3):
					isCorrect = False
					break

			if (not isIncreasing):
				if (check >= 0 or check < -3):
					isCorrect = False
					break

		if (isCorrect):
			result += 1

	return result

if __name__ == '__main__':
	print(partOne())
