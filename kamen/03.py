import websocket

ws = websocket.create_connection("ws://kamen.protab.cz/play/oof2win2")
will_end_next_turn = False

holding = {}

next_action = None

def set_choice(key: str, choice: str):
	holding[key] = choice

def get_own_choice():
	if "oof2win2" not in holding:
		return None
	return holding["oof2win2"]

while True:
	print()
	data = ws.recv()
	print(data, end=" ")
	
	if will_end_next_turn: break
	if data == "KONEC":
		will_end_next_turn = True
		continue
	elif data == "RESET":
		next_action = None
		holding.clear()
		continue
	elif data == "???":
		if next_action == None:
			choice = get_own_choice()
			if choice is None:
				ws.send("kámen")
				print("kámen")
			else:
				ws.send("skóruje")
				print("skóruje", end=" ")
		else:
			ws.send(next_action)
			print(next_action, end=" ")
		continue

	line = data.split(";")
	print(line, end=" ")
	
	action = line[1]
	color = line[2]
	agent = line[3]

	key = f"{agent}"
	
	if action in ["kámen", "nůžky", "papír"]:
		set_choice(key, action)
	elif action == "obnovuje":
		set_choice(key, None)
		if agent == "oof2win2":
			next_action = "obnovuje"
	
	ws.send("kámen")