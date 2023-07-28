import os
import subprocess

suites = os.listdir("suites")
suites.sort()

for suite in suites:
	# print(f"running suite {suite}")
	with open(f"suites/{suite}", "r") as f:
		inputlines = f.read()
	data = subprocess.run(["python3", "02.py"], input=inputlines.encode(), capture_output=True)
	lines = data.stdout.splitlines()
	if lines[0].endswith(b"oof2win2"):
		print(f"✅ passed suite {suite}")
		pass
	else:
		print(f"❌ failed suite {suite}")