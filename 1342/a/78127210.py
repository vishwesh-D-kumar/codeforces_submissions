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
	x,y=I()
	a,b=I()
	x,y=max(x,y),min(x,y)
	print(min(y*b+a*(x-y),(y+x)*a))
	



