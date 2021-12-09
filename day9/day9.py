area = []

with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		area.append([int(c) for c in line])

risk = 0
low_points = []

for y, row in enumerate(area):
	for x, cell in enumerate(row):
		is_low_point = True
		if x > 0:
			is_low_point = is_low_point and area[y][x-1] > cell
		if y > 0:
			is_low_point = is_low_point and area[y-1][x] > cell
		if x < len(row)-1:
			is_low_point = is_low_point and area[y][x+1] > cell
		if y < len(area)-1:
			is_low_point = is_low_point and area[y+1][x] > cell
		if is_low_point:
			risk += cell + 1
			low_points.append((x, y))

width = len(area[0])
height = len(area)

sizes = []

for x, y in low_points:
	size = -1  # idk why this
	current_added = set()
	stack = [(x, y)]

	while stack:
		_x, _y = stack.pop()
		size += 1

		if _x > 0 and (_x-1, _y) not in current_added:
			if area[_y][_x-1] != 9:
				stack.append((_x-1, _y))
			current_added.add((_x-1, _y))

		if _y > 0 and (_x, _y-1) not in current_added:
			if area[_y-1][_x] != 9:
				stack.append((_x, _y-1))
			current_added.add((_x, _y-1))

		if _x < width-1 and (_x+1, _y) not in current_added:
			if area[_y][_x+1] != 9:
				stack.append((_x+1, _y))
			current_added.add((_x+1, _y))

		if _y < height-1 and (_x, _y+1) not in current_added:
			if area[_y+1][_x] != 9:
				stack.append((_x, _y+1))
			current_added.add((_x, _y+1))

	sizes.append(size)


print(sorted(sizes)[-3:])
