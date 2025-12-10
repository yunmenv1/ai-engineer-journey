numbers=[1,2,3,4,5]
print("numbers:")
for n in numbers:
	print(n)

total=0
for n in numbers:
	total +=n
	print("total:",total)

squares =[]
for n in numbers:
	squares.append(n*n)
print("squares:", squares)

student = {
    "name": "Yunmen",
    "age": 17,
    "city": "PA"
}

print("Name:", student["name"])
print("Age:", student["age"])

student["favorite_language"] = "Python"

for key, value in student.items():
    print(key, "=>", value)


