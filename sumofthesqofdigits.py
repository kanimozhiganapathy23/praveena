n=input()
a=list(n)
b=len(a)
sum=0
for i in range(0,b):
	sq=int(a[i])**2
	sum=sum+sq
print(sum)
