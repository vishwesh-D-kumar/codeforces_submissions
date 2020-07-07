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
def rec(i):
	if dp[i]!=-1:
		return dp[i]
	m=0
	for j in range(2*i,n+1,i):
		
		if arr[j]>arr[i]:
			# print(i,j)
			# print(rec(j))
			m=max(rec(j),m)
	# print(i,m)
	dp[i]=m+1
	return dp[i]

for __ in range(int(input())):
	n=int(input())
	arr=[0]+I()
	dp=[-1]*(n+1)
	
	for i in range(1,n+1):
		if dp[i]!=-1:continue
		rec(i)
	# print(dp)
	print(max(dp))





