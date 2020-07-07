import sys
# input = sys.stdin.buffer.readline
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a

for __ in range(int(input())):
	arr=input()
	n=len(arr)
	poss=[]
	i=0
	while(i<n-1 and arr[i]==arr[i+1]):
		i+=1
	i+=1
	# print(i,"%")
	ans=n+1
	while(i<n-1):
		prev=arr[i-1]
		c=1
		while(i<n-1 and arr[i]==arr[i+1]):
			i+=1
			c+=1
		
		i+=1
		if i>n-1:break
		nex=arr[i]
		if prev!=nex:
			ans=min(ans,c+2)
	print(ans) if ans<n+1 else print(0)




