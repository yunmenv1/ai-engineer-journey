filename="notes.txt"
with open(filename,"r") as f:
	text=f.read()
lines=text.splitlines()
words=text.split()
print(f"lines:{len(lines)}")
print(f"words:{len(words)}")
