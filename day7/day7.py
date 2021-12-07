crab_pos = []

with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		crab_pos = [int(i) for i in line.split(",")]

fuel = min((sum(map(lambda crab: abs(crab - i), crab_pos)) for i in range(max(crab_pos))))
fuel2 = min((sum(map(lambda crab: abs(crab - i) * (abs(crab - i) + 1) // 2, crab_pos)) for i in range(max(crab_pos))))

print(fuel)
print(fuel2)
