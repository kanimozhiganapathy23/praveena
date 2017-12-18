n=input()
a=0
b=1
print(a)
print(b)
if(n<0):
	print("Enter a valid number")
elif(n==0):
	print("Fibonacci series is 0")
else:
	for i in range(1,n):
		c=a+b
		a=b
		b=c
		print(b)
