import sys
input = sys.stdin.buffer.readline
from math import sqrt,ceil
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a


for __ in range(int(input())):
	n,k=I()
	if n%2==0:
		print(n+2*k)
		continue

	f=0
	least=n
	for i in range(2,n):
		if n%i==0:
			f=1
			least=i
			break
	print(n+least+2*(k-1))





