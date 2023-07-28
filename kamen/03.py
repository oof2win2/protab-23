import sys
import websocket
import os

ws = websocket.create_connection("ws://kamen.protab.cz/play/oof2win2")

holding_item = None
end_next = False

options = ['nůžky', 'papír', 'nůžky', 'papír', 'papír', 'nůžky', 'kámen', 'nůžky']

outstr = ""
i = 0
confirmed = 0
suite = -1

# all_lines = []

while True:
	data = ws.recv()
	# print(data)
	
	if data == "RESET":
		holding_item = None
		if suite != -1:
			print(f"RESET {suite}")
			with open(f"./suites/{suite}.in", "w") as f:
				f.truncate()
				f.write(outstr)
		outstr = ""
		suite += 1
		i = 0
		continue
	if end_next:
		print(f"RESET {suite}")
		print(f"END {data}", file=sys.stderr)
		suite += 1
		break
	if data == "KONEC":
		end_next = True
		continue

	if data == "???":
		if holding_item is None:
			choice = options[i]
			# DEBUG
			# print(choice)
			i += 1
			holding_item = choice
			ws.send(choice)
			# DEBUG
		else:
			choice = ""
			if confirmed < len(options):
				choice = "skóruje"
			else:
				choice = "bojuje"
			# print(choice)
			ws.send(choice)
		continue

	outstr += data + "\n"

	line = data.strip().split(";")
	prev_time = int(line[0])
	action = line[1]
	color = line[2]
	agent = line[3]
	# print(data)
	if agent == "oof2win2":
		# print(data)
		pass
	
	# debug out
	# print(data)

	if agent == "oof2win2":
		if action == "skóruje":
			holding_item = None
		elif action == "bojuje":
			# holding_item = None
			pass
		elif action == "obnovuje":
			# the item stays after you revive yourself
			pass
		elif action in ["kámen", "nůžky", "papír"]:
			confirmed += 1
			

with open(f"./suites/{suite}.in", "w") as f:
	f.truncate()
	f.write(outstr)