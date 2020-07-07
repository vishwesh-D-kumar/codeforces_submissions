import sys
from collections import Counter
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
	n=int(input())

	a=I()
	if n==1:
		print(0)
		continue

	c=Counter(a)
	comm=c.most_common(1)
	l=len(c.keys())
	x=1
	ele=comm[0]
	if l-1>=ele[1]:
		print(ele[1])
	else:
		if l>=ele[1]-1:
			print(ele[1]-1)
		else:
			print(l)
				# break



