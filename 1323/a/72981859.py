def I(): return(list(map(int,input().split())))
for __ in range(int(input())):
	n=int(input())
	x=I()
	f=0
	for i in range(n):
		if x[i]%2==0:
			f=1
			break
	if f:
		print(1)
		print(i+1)
	else:
		if n==1:
			print(-1)
		else:
			print(2)
			print(1,2)