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
	mindist=arr[1]-arr[0]
	minidx=0
	# for i in range(n-1):
	# 	if mindist>arr[i+1]-arr[i]:
	# 		mindist=arr[i+1]-arr[i]
	# 		minidx=i
	# print(*arr[minidx:]+arr[:minidx][::-1])
	ans=[-1]*n
	j=n-1
	l=0
	r=n-1
	while(j>=0):
		ans[j]=arr[l]
		l+=1
		j-=1
		if j<0:break
		ans[j]=arr[r]
		r-=1
		j-=1
	print(*ans)


