l = []

with open("input.txt") as f:
	for line in f.readlines():
		l.append(int(line))

increased = 0
last = []
last_sum = 0
for d in l:
	last.append(d)
	if len(last) < 3:
		continue
	elif len(last) > 3:
		last.pop(0)
	if last_sum == 0:
		last_sum = sum(last)
	if last_sum < sum(last):
		increased += 1
	last_sum = sum(last)

print(increased)