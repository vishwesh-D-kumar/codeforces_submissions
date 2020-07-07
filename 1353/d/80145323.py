import sys
import heapq 
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
	li=[(-n,0,n-1)]
	heapq.heapify(li)
	arr=[-1]*n
	c=1
	while(li):
		x,l,r=heapq.heappop(li)
		x=-x
		idx=(l+r)//2
		arr[idx]=c
		c+=1
		if idx>l:
			heapq.heappush(li,(-(idx-1-l+1),l,idx-1))
		if idx<r:
			heapq.heappush(li,(-(r-idx),idx+1,r))
	print(*arr)





