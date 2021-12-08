vals = []

with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip()
		split = line.split(" | ")
		signal = split[0].split()
		output = split[1].split()
		vals.append((signal, output))

t = 0

for signals, outs in vals:
	mapping = {}
	r_mapping = {}

	new_signals = []
	for s in signals:
		k = "".join(sorted(list(s)))
		new_signals.append(k)

	new_outs = []
	for s in outs:
		k = "".join(sorted(list(s)))
		new_outs.append(k)

	for s in new_signals:
		if len(s) == 2:
			mapping[s] = "1"
			r_mapping[1] = s
		elif len(s) == 4:
			mapping[s] = "4"
			r_mapping[4] = s
		elif len(s) == 3:
			mapping[s] = "7"
			r_mapping[7] = s
		elif len(s) == 7:
			mapping[s] = "8"
			r_mapping[8] = s

	for s in filter(lambda c: len(c) == 6, new_signals):
		if len(set(s).intersection(set(r_mapping[4]))) == 4:
			mapping[s] = "9"
			r_mapping[9] = s

		elif len(set(s).intersection(set(r_mapping[1]))) == 2:
			mapping[s] = "0"
			r_mapping[0] = s

		else:
			mapping[s] = "6"
			r_mapping[6] = s

	for s in filter(lambda c: len(c) == 5, new_signals):
		if len(set(s).difference(set(r_mapping[1]))) == 3:
			mapping[s] = "3"
			r_mapping[3] = s

		elif len(set(s).union(set(r_mapping[4]))) == 7:
			mapping[s] = "2"
			r_mapping[2] = s

		else:
			mapping[s] = "5"
			r_mapping[5] = s

	out = ""
	for s in new_outs:
		out += mapping[s]
	t += int(out)

print(t)
