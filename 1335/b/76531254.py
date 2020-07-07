import sys
input = sys.stdin.buffer.readline
from collections import Counter
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a

for __ in range(int(input())):
	n,a,b=I()

	s="a"*(a-b+1)
	for i in range(b-1):
		s+=chr(98+i)
	# print(s)
	ans=""
	ans=(n//len(s))*s+s[:n%len(s)]
	print(ans)

