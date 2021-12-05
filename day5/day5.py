l = []

with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		coords = line.split(" -> ")
		p0 = tuple(int(i) for i in coords[0].split(","))
		p1 = tuple(int(i) for i in coords[1].split(","))
		l.append([p0, p1])

covered_points = set()
multicovered_points = set()

for line in l:
	if line[0][0] == line[1][0]:
		# vertical
		p0 = line[0][1]
		p1 = line[1][1]
		for i in range(min(p0, p1), max(p0, p1) + 1):
			point = (line[0][0], i)
			if point in covered_points:
				multicovered_points.add(point)
			covered_points.add(point)
	elif line[0][1] == line[1][1]:
		# horizontal
		p0 = line[0][0]
		p1 = line[1][0]
		for i in range(min(p0, p1), max(p0, p1) + 1):
			point = (i, line[0][1])
			if point in covered_points:
				multicovered_points.add(point)
			covered_points.add(point)
	else:
		#diagonal
		p0 = min(line)
		p1 = max(line)
		cur_p = p0
		direction = 1 if p1[1] > p0[1] else -1
		while cur_p <= p1:
			if cur_p in covered_points:
				multicovered_points.add(cur_p)
			covered_points.add(cur_p)
			cur_p = (cur_p[0] + 1, cur_p[1] + direction)

print(len(multicovered_points))
