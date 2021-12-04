l = []
ns = []

with open("input.txt") as f:
	i = 0
	bid = 0
	board = []
	for line in f.readlines():
		line = line.strip()
		if i == 0:
			i += 1
			ns = [int(i) for i in line.split(",")]
		elif line != "" and i != 0:
			row = []
			for j in line.split():
				if j != "":
					row.append(int(j))
			board.append(row)
		elif line == "":
			l.append(board)
			board = []

table = []

for board in l:
	t = list(zip(*board)) # transpose to get columns
	cur_set = set()
	done = False
	for i, n in enumerate(ns):
		cur_set.add(n)
		turns = i
		score = 0
		for row in board:
			if set(row).issubset(cur_set):
				score = n * sum( x for x in ( sum(filter(lambda x: x not in cur_set, r)) for r in board ) )
				done = True
				break
		for col in t:
			if set(col).issubset(cur_set):
				score = n * sum( x for x in ( sum(filter(lambda x: x not in cur_set, r)) for r in board ) )
				done = True
				break
		if done:
			table.append((turns, score))
			break

print(min(table)) # part 1
print(max(table)) # part 2