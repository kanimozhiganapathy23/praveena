n=input()
a=n.split(" ")
b=len(a[0])
c=len(a[1])
if(b==c):
	for i in range(0,b):
		if(a[0][i]!=a[1][i]):
			a[0]=a[0].replace(a[0][i],a[1][i])
if a[0]==a[1]:
	print("Yes")
else:
	print("No")
	
	
	
	
