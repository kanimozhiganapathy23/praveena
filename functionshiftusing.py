def main():
	n=input()
	a=n.split(" ")
	N=int(a[0])
	k=int(a[1])
	l=[]
	for i in range(0,N):
		b=int(input())
		l.append(b)
	l=shift(N,l,k)
	print(l)
def shift(N,l,k):
		for i in range(k):
			l=l[N-1:]+l[:N-1]
		return l
main()
