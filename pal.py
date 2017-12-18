n=int(raw_input())
num=n
sum=0
while(num>0):
	rem=num%10
	sum=sum*10+rem
	num=num/10
if(sum==n):
	print('palindrome')
else:
	print('not palindrome')
