n=input()
a=n.split(" ")
N=int(a[0])
k=int(a[1])
b=input()
l=b.split(" ")
for i in range(k):
	l=l[N-1:]+l[:N-1]
print(" ".join(l))
