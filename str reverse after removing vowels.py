n=int(input())
m=input()
a=list(m)
b=[]
l=["a","e","i","o","u"]
for i in a:
	if i not in l:
		b.append(i)
n=b[::-1]
print("".join(n))
