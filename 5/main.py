def partOne():
	rules = {}
	# Read page ordering rules
	with open("input1.txt") as f1:
		for line in f1:
			nums = [int(x) for x in line.split("|")]
			if nums[0] in rules:
				rules[nums[0]] = rules[nums[0]] + [nums[1]]
			else:
				rules[nums[0]] = [nums[1]]
	
	updates =[]
	# Read pages to produce updates
	with open("input2.txt") as f2:
		updates = f2.read().strip().split("\n")
	
	result = 0
	# Loop through all updates
	for pages in updates:
		listOfPages = [int(x) for x in pages.split(",")]
		isCorrect = True

		# Loop through all pages in an update
		for i in range(len(listOfPages) - 1, 0, -1):
			curr = listOfPages[i]
			if curr in rules:
				blacklisted = rules[curr]
			else:
				blacklisted = []
			
			# Check that each page is valid
			for j in range(i):
				if listOfPages[j] in blacklisted:
					isCorrect = False
					break
			
			if not isCorrect:
				break
			
		if isCorrect:
			middle = listOfPages[int(len(listOfPages) / 2)]
			result += middle
	
	return result



if __name__ == '__main__':
	print(partOne())
