import sys
input = sys.stdin.buffer.readline
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a

for __ in range(int(input())):
	n,x=I()
	arr=I()
	f=0
	for i in range(n):
		if arr[i]%x!=0:
			f=1
			break
	if not f:
		print(-1)
	else:
		s=sum(arr)
		if s%x:
			print(n)
		else:
			c1=0
			for i in reversed(range(n)):
				c1+=1
				if arr[i]%x:
					break
						
			c2=0
			for i in range(n):
				c2+=1
				if arr[i]%x:
					break
			print(n-min(c1,c2))




	



