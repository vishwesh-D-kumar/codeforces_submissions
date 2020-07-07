def I(): return(list(map(int,input().split())))
def rec(l,r):
	numavens=getnums(l,r)
	# print(numavens,l,r)
	
	if numavens==0:return a
	if l==r:return b*numavens
	mid=(r-l)//2+l
	return min(((r-l)+1)*numavens*b,rec(l,mid)+rec(mid+1,r))
def getnums(l,r):
	if l==0:return get(r)
	return get(r)-get(l-1)
def get(t):
	l=0
	r=k-1
	# print(x)
	while(l<=r):
		mid=(r-l)//2+l
		if x[mid]<=t:l=mid+1
		else: r=mid-1
	# print(l,t)
	return l

n,k,a,b=I()
x=I()
x.sort()

l=1
r=2**n
print(rec(l,r))


