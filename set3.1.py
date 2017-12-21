def ssumofap( a, d, n):
	sum = 0
	i  = 0
	while( i < n ):
		sum = sum + a
		a = a + d
		i = i + 1
            return(sum)
a = 1
d = 2
n = 4
print(ssumofap( a, d, n))
