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
	n=int(input())
	arr=I()
	if n==1:print(0)
	else:
		maxdiff=0
		mins=[0]*n
		m=arr[-1]
		usedic={}
		mins[-1]=m
		for i in reversed(range(n-1)):
			mins[i]=min(mins[i+1],arr[i])
		i=0
		while(i<n-1):
			if arr[i]<=arr[i+1]:
				i+=1
				continue
			else:
				maxdiff=max(arr[i]-mins[i],maxdiff)
				usedic[maxdiff]=usedic.get(arr[i]-mins[i],0)+1
				i+=1
		if maxdiff==0:print(0)
		else:
			# print(maxdiff,usedic)

			ans=math.log(maxdiff,2)
			if ans==math.ceil(ans):
				ans=math.ceil(ans)+1
			else:
				ans=math.ceil(ans)
			# if usedic[maxdiff]>1:ans+=usedic[maxdiff]-1
			print(ans)

		# if i==n-1:print(0)
		# else:
		# 	j=i
		# 	i+=1
		# 	m=arr[i]
		# 	while(i<n):
		# 		m=min(m,arr[i])
		# 		i+=1
		# 	print(math.ceil(math.log(arr[j]-m,2))+1)
		






