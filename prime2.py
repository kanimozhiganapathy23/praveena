n=input()
m=input()
for num in range(n,m):
	if num>1:
		for i in range(2,num):
			if(num%i==0):
				break
		else:
            		 print(num)
