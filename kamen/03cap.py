from sys import stdin

lines = []

for line in stdin:
	if line.startswith("END"):
		print(line.strip())
	if line.startswith("RESET"):
		id = line.split(" ")[1].strip()
		print(f"RESET {id}")
		with open(f"./suites/{id}.in", "w") as f:
			f.truncate()
			f.write("\n".join(lines))
		lines = []
	else:
		lines.append(line.strip())