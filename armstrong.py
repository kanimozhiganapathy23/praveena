n=input()
num=n
sum=0
if(num>0):
	rem=num%10
	temp=rem**3
	sum=sum+temp
	num=num/10
if(n==sum):
	    print('Armstrong number')
else:
                print('Not a Armstrong Number')		
