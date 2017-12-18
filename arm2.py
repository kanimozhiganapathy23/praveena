a=input()
b=input()
sum=0
for n in range(a,b):
	num=n
	sum=0
while(num>0):
	rem = num%10
	temp = rem**3
	sum = sum+temp
	num = num/10
if(n==sum):
	    print(n)
