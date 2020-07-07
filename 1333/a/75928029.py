def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a




for __ in range(int(input())):
	n,m=I()
	for i in range(n-1):
		print("B"*m)
	if n==1:print("B"*(m-2)+"W"+"B")
	else:print("B"*(m-1)+"W")