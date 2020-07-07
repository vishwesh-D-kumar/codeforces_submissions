n,l,r=[int(i)for i in input().split()]
#Min
if n<=l:
	print(n)
else:
	smin="1"*(n-l+1)
	ansmin=n-l+1
	c=2
	for i in range(l-1):
		smin+=str(c)
		ansmin+=c
		c*=2
	print(ansmin, end=" ")
#max:
s=""
ans=0
c=1
for i in range(r):
	s+=str(c)
	ans+=c
	c*=2
c//=2
# print(ans,c)
# print(s)
if r<n:
	ans+=(n-r)*c
print(ans)





