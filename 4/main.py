def partOne():
	# Generate all directions into tuples
	dd = generateDirections()

	ans = 0
	for i in range(row):
		for j in range(col):
			for d in dd:
				ans += has_xmas(i, j, d)
	
	return ans

def partTwo():
	ans = 0
	for i in range(row):
		for j in range(col):
			ans += has_xmas_2(i, j)

	return ans

	
def generateDirections():
	dd = []
	for x in range(-1, 2):
		for y in range(-1, 2):
			if (x == 0 and y == 0):
				continue
			dd.append((x, y))
	return dd

def has_xmas(i, j, d):
	dx, dy = d
	for k, z in enumerate("XMAS"):
		ix = i + (k * dx)
		jy = j + (k * dy)
		if (ix < 0 or jy < 0 or ix >= row or jy >= col):
			return False
		if (lines[ix][jy] != z):
			return False
	return True

def has_xmas_2(i, j):
	if not (1 <= i < row - 1 and 1 <= j < col - 1):
		return False
	
	if lines[i][j] != "A":
		return False
	
	diag_1 = lines[i - 1][j - 1] + lines[i + 1][j + 1]
	diag_2 = lines[i - 1][j + 1] + lines[i + 1][j - 1]

	return diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]


if __name__ == '__main__':
	# Read input and put into array
	with open("input.txt") as f:
		lines = f.read().strip().split("\n")
	row = len(lines)
	col = len(lines[0])

	print(partTwo())
