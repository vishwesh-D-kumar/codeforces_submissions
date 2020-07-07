t=int(input())
for baka in range(t):
	n,k=list(map(int,input().split()))
	a=list(map(int,input().split()))
	u=a[0]+k
	l=a[0]-k
	for i in range(1,len(a)):
		u=min(a[i]+k,u)
		l=max(a[i]-k,l)
		if l>u:
			break
	if l>u:
		print(-1)
	else:
		print(u)

