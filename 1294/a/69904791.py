def I(): return(list(map(int,input().split())))
for lol in range(int(input())):
	a,b,c,n=I()
	# x=(n+a+b+c)//3
	m=max(a,b,c)
	minReqd=3*m-(a+b+c)
	if ((n-minReqd)%3 or n-minReqd<0):
		print("NO")
	else:
		print("YES")

