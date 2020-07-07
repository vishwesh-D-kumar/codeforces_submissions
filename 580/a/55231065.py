input()
x=list(map(int,input().split()))

l=0
r=1
c=1
while(l<len(x) and r<len(x)):

	if x[r]>=x[r-1]:
		r+=1
	else:
		l=r
		r=l+1
	if c<r-l:
			c=r-l
print(c)

