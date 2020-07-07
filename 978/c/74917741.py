def I(): return(list(map(int,input().split())))
n,m=I()
a,b=I(),I()

arr=[0]*(n+1)
arr[0]=a[0]
for i in range(n-1):
	arr[i+1]=arr[i]+a[i+1]
currl=0
for i in range(m):

	l=currl
	r=n-1

	while(l<=r):
		mid=(r-l)//2+l
		if arr[mid]<b[i]:l=mid+1
		else: r=mid-1

	print(l+1,b[i]-arr[l-1])
	currl=l
