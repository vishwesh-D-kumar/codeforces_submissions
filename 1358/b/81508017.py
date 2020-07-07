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
	n=int(input())
	arr=I()
	arr.sort()
	currmax=0
	ans=0
	for i in range(n):
		currmax=max(arr[i],currmax)
		if currmax<=(i+1):ans=i+1
	print(ans+1)
	



