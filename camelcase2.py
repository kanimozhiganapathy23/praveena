n=input()
l=[]
b=n.lower()
a=b.split(" ")
for i in a:
 	c=i[0].upper()+i[1:]
 	l.append(c)
print(" ".join(l))
 
