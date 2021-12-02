l = []

with open("input.txt") as f:
	for line in f.readlines():
		ls = line.split()
		l.append((ls[0], int(ls[1])))

h = 0
a = 0
d = 0

for instr, n in l:
	if instr == "forward":
		h += n
		d += a * n
	elif instr == "down":
		a += n
	elif instr == "up":
		a -= n

print(h * d)
