ages = {age: 0 for age in range(9)}

with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		for age in line.split(","):
			ages[int(age)] += 1

new_ages = {age: 0 for age in range(9)}
for i in range(256):
	new_ages[6] = ages[0]
	for age, count in ages.items():
		new_age = age - 1
		if new_age < 0:
			new_age = 8
		new_ages[new_age] += count
	ages = new_ages
	new_ages = {age: 0 for age in range(9)}

print(sum(ages.values()))
