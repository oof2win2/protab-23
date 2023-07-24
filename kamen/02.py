#!/usr/bin/env python3

from sys import stdin

lines = []

# read all of the stdin into the variable rawdata as a list of lines until EOF

for line in stdin:
	lines.append(line.strip().split(";"))

choices = {}
scores = {}
color_scores = {}
usefulness = {}

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
	
	key = f"{color};{agent}"
	if key not in usefulness:
		usefulness[key] = 1
	else:
		usefulness[key] += 1

def renew(color: str, agent: str):
	key = f"{color};{agent}"
	if key not in usefulness:
		usefulness[key] = -1
	else:
		usefulness[key] -= 1
	
	set_choice(color, agent, None)

for line in lines:
	action = line[1]
	color = line[2]
	agent = line[3]

	key = f"{color};{agent}"
	if key not in usefulness:
		usefulness[key] = 0

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
		renew(color, agent)

# print(usefulness)
for pair in sorted(usefulness.items(), key=lambda x:x[1], reverse=True):
	print(pair[0])
	# print(sorted(usefulness[color].items(), key=lambda x:x[1], reverse=True))
