#!/usr/bin/env python3

from sys import stdin

lines = []

for line in stdin:
	lines.append(line.strip().split(";"))
# with open("/Users/oof2win2/git/protab-23/kamen/02.in", "r") as f:
# 	for line in f.readlines():
# 		lines.append(line.strip().split(";"))

past_actions = {}

for line in lines:
	action = line[1]
	color = line[2]
	agent = line[3]

	key = f"{color};{agent}"

	if key not in past_actions:
		past_actions[key] = [line]
	else:
		past_actions[key].append(line)

found_own = []

options = ['nůžky', 'papír', 'nůžky', 'papír', 'papír', 'nůžky', 'kámen', 'nůžky']

for key in past_actions:
	actions = past_actions[key]
	i = 0
	for line in actions:
		action = line[1]
		agent = line[3]
		if action == "obnovuje":
			continue
		if action == "skóruje":
			continue
		if action == "bojuje":
			# if there haven't been that many actions sent as i hav options, it's not mee
			# we want to score and send the whole sequence before doing nothing
			# by fighting
			if i != len(options):
				break
			continue
		else:
			# kamen, nuzky, papir

			# if this agent has more actions than i have options, then it's not me
			if i > len(options):
				break

			# if the chosen action is not in line with my choices, it's not me
			choice = options[i]
			if action != choice:
				break
			i += 1
	else:
		# if it didnt break then it will run this
		if i == len(options) or i == 1:
			found_own.append(key)

# print(f"found {found_own}")
for item in found_own:
	print(item)
for key in past_actions:
	if key not in found_own:
		print(key)