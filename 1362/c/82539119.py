import sys
input = sys.stdin.buffer.readline
from math import log,ceil
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a
def precalc():
	arr=[0]*61
	curr=1
	for i in range(61):
		arr[i]=curr
		curr*=2
	return arr
powers=precalc()
for __ in range(int(input())):
	m=int(input())
	n=ceil(log(m,2))+1
	s=0
	for i in range(n):
		pow2=powers[i]
		# if m%pow2:
		# 	currs=m//pow2
		# else:
		# 	currs=m//pow2+1
		# print(pow2)
		s+=(m//pow2)
	print(s)






