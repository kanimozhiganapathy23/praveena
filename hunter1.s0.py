n=int(input())
m=input()
l=m.split(" ")
s=set(l)
lst=[]
L=[]
for i in s:
	c=0
	for j in l:
		if(i==j):
			c=c+1
	if(c>1):
		lst.append(i)
	
lst=sorted(lst)
if(len(lst)==0):
	print("unique")
else:
	print(" ".join(lst))

