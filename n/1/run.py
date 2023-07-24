import requests

base_url = "https://krokodyl.protab.mvolfik.com/"
next_url = base_url

letters = []

id = 0

seen = set()

while True:
	dat = requests.get(next_url, allow_redirects=False, timeout=None)
	print(dat, dat.headers['Location'])
	_, getid, letter = dat.headers['Location'].split('/')
	id = int(getid) + 1
	if id in seen:
		break
	seen.add(id)
	next_url = base_url + dat.headers['Location']
	letters.append(letter)
    
print(''.join(letters))