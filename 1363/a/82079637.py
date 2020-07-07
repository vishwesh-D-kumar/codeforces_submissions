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
	odds=0
	evens=0
	for i in range(n):
		if arr[i]%2:
			odds+=1
		else:
			evens+=1
	if x%2:
		c=2
		i=0
	else:
		c=2
		i=1
	f=0
	for e in range(i,min(evens+1,x+1),c):
		if odds>=(x-e):
			f=1
	if f:
		print("Yes")
	else:
		print("No")





