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
	n,m,k=I()
	if n//k>=m:
		print(m)
	else:
		left=m-n//k
		# print(left//(k-1))
		print(n//k-ceil(left/(k-1)))
	



