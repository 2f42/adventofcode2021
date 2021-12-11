
area = []

with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		area.append(list(int(i) for i in line))

def has_bigger_than_9():
	for row in area:
		for cell in row:
			if cell > 9:
				return True
	return False

def step():
	global area
	new_area = [[i for i in row] for row in area]
	flashes = []
	flashed = set()
	
	for y, row in enumerate(area):
		for x, _ in enumerate(row):
			new_area[y][x] += 1
			if new_area[y][x] > 9:
				flashes.append((x, y))
				flashed.add((x, y))

	while flashes:
		x, y = flashes.pop()
		to_be_flashed = []
		for dy in range(3):
			for dx in range(3):
				if dy == dx and dx == 1:
					continue
				if x+dx-1 > 9 or x+dx-1 < 0:
					continue
				if y+dy-1 > 9 or y+dy-1 < 0:
					continue
				to_be_flashed.append((x+dx-1, y+dy-1))

		for x, y in to_be_flashed:
			if (x, y) in flashed:
				continue
			new_area[y][x] += 1
			if new_area[y][x] > 9:
				flashes.append((x, y))
				flashed.add((x, y))

	for x, y in flashed:
		new_area[y][x] = 0

	if len(flashed) == 100:
		print("in sync!")
		return False

	area = new_area
	return True

i = 1
while step():
	i += 1
print(i)