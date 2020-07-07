import sys
from math import log2 as log
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
	a,b=I()
	b,a=max(a,b),min(a,b)

	if b%a!=0:
		print(-1)
		continue
	x=log((b//a))

	if b//a!=2**int(x):
		print(-1)
		continue
	else:
		x=int(x)
		m=0
		m+=x//3
		x%=3
		m+=x//2
		x%=2
		m+=x
		print(m)

	



