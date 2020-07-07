def I(): return(list(map(int,input().split())))
def f(k):
	s=0
	if k-idx>1:
		s-=(k-idx-1)*(k-idx)//2
	if k-(n-idx-1)>1:
		s-=(k-(n-idx-1)-1)*(k-(n-idx-1))//2
	s+=k**2
	return s

n,m,idx=I()
idx-=1
m=m-n
l=0
r=m
while(l<=r):
	mid=(r-l)//2+l
	if f(mid)<=m:l=mid+1
	else:r=mid-1
	# print(f(mid),mid)
print(r+1)

	
