filename="notes.txt"

with open(filename,"r")as f:
	text=f.read().lower()

words=text.split()

freq={}

for w in words:
	if w in freq:
		freq[w]+=1
	else:
		freq[w]=1

print("word frequencies:")
for word, count in freq.items():
	print(word,"=>",count)
	