n=input()
a=list(n)
b=set(a)
temp=0
for i in b:
	c=0
	for j in a:
		if i==j:
			
			c=c+1
			if(c>temp):
				temp=c
				rep=j
print(rep)
