n=int(input())
m=int(input())
for i in range(n,m+1):
	if(i==2):
		print(i)
	for j in (2,i):
		if(i%j==0):
			break
		else:
			print(i)
