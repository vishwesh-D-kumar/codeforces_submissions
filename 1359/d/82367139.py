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

# for __ in range(int(input())):
n=int(input())
arr=I()
ans=0

for i in range(-32,33):
	maxs=-33
	f=0
	currmax=-33
	for j in range(n):
		if arr[j]==i:
			f=1
		if arr[j]>i:
			currmax=-33
			continue
		currmax=max(arr[j]+currmax,arr[j])
		maxs=max(currmax,maxs)
	if f:
		ans=max(maxs-i,ans)
print(ans)



