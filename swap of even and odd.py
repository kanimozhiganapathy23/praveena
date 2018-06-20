n=input()
a=list(n)
c=len(a)
if(c==4):
	 a[0],a[1]=a[1],a[0]
	 a[2], a[3]=a[3],a[2]
op="".join(a)
print(op)

	

