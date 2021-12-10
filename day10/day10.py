illegal_table = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
}

auto_table = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4
}

pairs = {
	"(": ")",
	"[": "]",
	"{": "}",
	"<": ">"
}

lines = []

with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		lines.append(line)

score = 0
autocomplete = []

for line in lines:
	openers = []
	for c in line:
		if c in pairs.keys():
			openers.append(c)
		elif c != pairs[openers[-1]]:
			score += illegal_table[c]
			break
		else:
			openers.pop()
	else:
		t_score = 0
		while openers:
			t_score *= 5
			t_score += auto_table[pairs[openers.pop()]]
		autocomplete.append(t_score)

print(score)
print(sorted(autocomplete)[len(autocomplete)//2])