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
	c=0
	ans=[]
	i=0
	while(i<n):
		if i==n-1:
			ans.append(arr[i])
			break
		ans.append(arr[i])
		# print(ans)
		if arr[i]>arr[i+1]:
			# j=i
			while (i<n-1 and arr[i]>=arr[i+1]):
				i+=1
			# print(i)
		else:
			while (i<n-1 and arr[i]<=arr[i+1]):
				i+=1
			# print(i)
			# ans.append(arr[i])
	print(len(ans))
	print(*ans)



