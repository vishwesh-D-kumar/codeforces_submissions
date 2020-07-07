import sys
from math import ceil
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
	a,b,c,d=I()
	if b>=a:
		print(b)
		continue
	if c<=d:
		print(-1)
		continue
	a-=b
	print(ceil(a/(c-d))*c+b)
	



