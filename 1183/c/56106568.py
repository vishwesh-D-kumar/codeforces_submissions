t=int(input())
for baka in range(t):
	k,n,a,b=list(map(int,input().split()))
	if k-n*b<=0:
		print(-1)
	else:
		x=(k-n*b)
		if x%(a-b)==0:
			print(min(n,(k-n*b)//(a-b)-1))
		else:
			print(min(n,(k-n*b)//(a-b)))


		
