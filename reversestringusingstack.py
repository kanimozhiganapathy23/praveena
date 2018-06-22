n=input()
stack=list(n)
l=[]
list=stack[:]
for i in n:
	l.append(stack.pop())
print("".join(l))
