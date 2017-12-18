n=int(raw_input())
if (n>1):
	for i in range(2,n):
		if (n%i==0):
			print('not a prime number')
			break
		else:
			print('prime number')
else:
     print('enter a valid number')
