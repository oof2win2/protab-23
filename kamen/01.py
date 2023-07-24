lines = []

with open("01.in", "r") as file:
	rawdata = file.readlines()
	for line in rawdata:
		lines.append(line.strip().split(";"))

choices = {}
scores = {}
color_scores = {}

def set_choice(color: str, agent: str, choice: str):
	if color not in choices:
		choices[color] = dict()
	choices[color][agent] = choice

def get_choice(color: str, agent: str) -> str:
	if color not in choices:
		return None
	if agent not in choices[color]:
		return None
	return choices[color][agent]

def score(color: str, agent: str, pts: int):
	if color not in scores:
		scores[color] = dict()
	if agent not in scores[color]:
		scores[color][agent] = pts
	else:
		scores[color][agent] += pts
	
	if color not in color_scores:
		color_scores[color] = pts
	else:
		color_scores[color] += pts

for line in lines:
	action = line[1]
	color = line[2]
	agent = line[3]

	if action in ["kámen", "nůžky", "papír"]:
		set_choice(color, agent, action)
	elif action == "skóruje":
		choice = get_choice(color, agent)
		if choice == "kámen":
			score(color, agent, 5)
		elif choice == "papír":
			score(color, agent, 6)
		elif choice == "nůžky":
			score(color, agent, 7)
	elif action == "obnovuje":
		pass

print(color_scores)
for pair in sorted(color_scores.items(), key=lambda x:x[1], reverse=True):
	color = pair[0]
	print(sorted(scores[color].items(), key=lambda x:x[1], reverse=True))