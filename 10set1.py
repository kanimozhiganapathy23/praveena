n=input()
a=n.split(" ")
n1=len(a[0])
n2=len(a[1])
print(a)
count=0
for i in range (0,n1):
	if(a[0][i]!=a[1][i]):
		count=count+1
if(count==1):
	print("yes")
else:
	print("no")
