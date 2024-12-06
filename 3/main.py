import re

def partOne():
	f = open("input.txt", "r")	
	multiplyList = []
	for line in f:
		multiplyList += re.findall("mul\(\d+,\d+\)", line)

	result = 0
	for expr in multiplyList:
		product = multiply(expr)
		result += product
	
	return result


def partTwo():
	f = open("input.txt", "r")
	multiplyList =[]
	for line in f:
		multiplyList += re.findall("(don't\(\))|(do\(\))|(mul\(\d+,\d+\))", line)

	result = 0;
	enabled = True
	for expr in multiplyList:
		if expr[0] == "don't()":
			enabled = False
			continue
		elif expr[1] == "do()":
			enabled = True
			continue

		if (enabled):
			result += multiply(expr[2])
	
	return result


def multiply(expr):
	integers = re.findall("\d+", expr)
	return int(integers[0]) * int(integers[1])

if __name__ == '__main__':
	print(partOne())
	print(partTwo())
