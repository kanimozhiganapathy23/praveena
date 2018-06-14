n=input()
l=list(n)
c=0
d=0
sum=0
for i in l:
	if(i.isdigit()):
		c=c+1
	elif(i.isalpha()):
		d=d+1
sum=c+d
print(sum)
print(len(l)-sum)
