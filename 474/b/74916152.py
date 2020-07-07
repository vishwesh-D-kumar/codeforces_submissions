def I(): return(list(map(int,input().split())))
n=int(input())
x=I()
m=int(input())
q=I()
arr=[0]*(n+1)
arr[0]=x[0]
for i in range(n-1):
	arr[i+1]=arr[i]+x[i+1]

for i in range(m):

	l=0
	r=n-1

	while(l<=r):
		mid=(r-l)//2+l
		if arr[mid]<q[i]:l=mid+1
		else:r=mid-1
	print(l+1)
