import sys
import math
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
	n,g,b=I()
	k=math.ceil(n/2)
	togetgood=math.ceil(k/g)*(g+b)
	extragood=(togetgood//(g+b))*g-k
	# print(togetgood,extragood)
	togetgood-=extragood+b
	print(max(n,togetgood))


