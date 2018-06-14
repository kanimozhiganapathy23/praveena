n=input()
a=n.split(" ")
temp=0
for i in range(0,len(a)):
	if(len(a[i])>temp):
		temp=len(a[i])
		word=a[i]

print(word)
