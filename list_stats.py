print("enter nubmers seperated by sapces:")
line=input("nubmers:")

parts=line.split()

if not parts:
	print("no nubmers entered")
else:
	numbers=[]
	for p in parts:
		try:
			numbers.append(float(p))
		except ValueError:
			print(f"skipping invalid value:{p}")

			if not numbers:
				print("no valid numbers")
			else:
				print("count:",len(numbers))
				print("min",min(numbers))
				print("max",max(numbers))
				print("average:", sum(numbers)/len(numbers))

