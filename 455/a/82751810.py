import sys
input = sys.stdin.buffer.readline
from collections import Counter
sys.setrecursionlimit(1000000)
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
		if a[i]:
			for j in range(i*i,n,i):
				a[j]=0
	return a
def rec(i):
	if i<0:
		return 0
	if dp[i]!=-1:return dp[i]
	if i==0:
		dp[i]=arr[i]*c[arr[i]]
	if arr[i-1]==arr[i]-1:
		dp[i]=max(rec(i-2)+arr[i]*c[arr[i]],rec(i-1))
	else:
		dp[i]=arr[i]*c[arr[i]]+rec(i-1)
	return dp[i]

n=int(input())
arr=I()
c=Counter(arr)
arr=sorted(list(set(arr)))
# print(arr)
n=len(arr)
dp=[-1]*n
# dp[0]=arr[0]*c[arr[0]]
for i in range(1,n):
	rec(i)
print(rec(n-1))
			
			
			
		