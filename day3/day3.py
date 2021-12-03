l = []

with open("input.txt") as f:
	for line in f.readlines():
		l.append(line.strip())

counts = {i: 0 for i in range(12)}
thresh = len(l) // 2

for i in l:
	for j, b in enumerate(i):
		if b == "1":
			counts[j] += 1

gammas = []
epsilons = []

for k in counts:
	if counts[k] >= thresh:
		gammas.append("1")
		epsilons.append("0")
	else:
		epsilons.append("1")
		gammas.append("0")

print(gammas)
print(epsilons)

gamma = int("".join(gammas), 2)
epsilon = int("".join(epsilons), 2)

nl = list(l)
print(len(nl))

for k in counts:
	lp = []
	if counts[k] < thresh:
		# 0 is more common than 1
		for i in nl:
			if i[k] == "0":
				lp.append(i)
	else:
		for i in nl:
			if i[k] == "1":
				lp.append(i)
	nl = lp

	counts = {i: 0 for i in range(12)}
	thresh = len(nl) // 2

	for i in nl:
		for j, b in enumerate(i):
			if b == "1":
				counts[j] += 1

	print(len(nl))
	if len(nl) == 1:
		print(k, nl)
		break

oxygen = int(nl[0], 2)

nl = list(l)
print(len(nl))

for k in counts:
	lp = []
	if counts[k] >= thresh:
		# 0 is less or as common as 1
		for i in nl:
			if i[k] == "0":
				lp.append(i)
	else:
		for i in nl:
			if i[k] == "1":
				lp.append(i)
	nl = lp

	counts = {i: 0 for i in range(12)}
	thresh = len(nl) // 2

	for i in nl:
		for j, b in enumerate(i):
			if b == "1":
				counts[j] += 1
	
	print(len(nl))
	if len(nl) == 1:
		print(k, nl)
		break

co2 = int(nl[0], 2)

print(oxygen, co2)
print(bin(oxygen), "\n", bin(co2))
print(oxygen * co2)

print(gamma * epsilon)