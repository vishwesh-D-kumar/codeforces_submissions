def I():return list(map(int,input().split()))
def bin(arr,t):
	l=0
	r=len(arr)-1
	while(l<=r):
		mid=l+(r-l)//2
		if arr[mid]>=t:r=mid-1
		else:l=mid+1
	return r
n=int(input())
a=I()
b=I()
s=[b[i]-a[i] for i in range(n)]

s.sort()
# print(s)
c=0
for i in range(n):
	j=bin(s,-s[i])
	# print(j)
	if j>i:j-=1

	c+=(j+1)
print(c//2)

