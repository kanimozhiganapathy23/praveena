n=int(input())
m=input()
l=m.split(" ")
s=set(l)
for i in s:
	c=0
	for j in l:
		if(i==j):
			c=c+1
	if(c==1):
		print(i)
