print("simple calculator")
a=float(input("enter first number"))
b=float(input("enter second number"))
op=input("choose operation(+,-,*,/):")

if op=="+":
	result==a+b
elif op=="-":
	result==a-b
elif op=="*":
	result=a*b
elif op=="/":
	if b==0:
		result="error:division by zero"
	else:
		result=a/b
else:
	result="unkonwn operation"
print ("result:", result)
