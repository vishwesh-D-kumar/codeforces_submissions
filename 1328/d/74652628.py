def I():return list(map(int,input().split()))



for __ in range(int(input())):
	n=int(input())
	
	x=I()
	f=0
	t=len(set(x))
	mark=0
	for i in range(n-1):
		if x[i]==x[i+1]:
			mark=i
			f=1
			break
	if x[0]==x[-1]:
		mark=n-1
		f=1

	if t==1:
		print(1)
		print(*[1]*n)
	else:
		s=[]
		if n%2:
			if f:
				print(2)
				col=1
				for i in range(n):
					s.append(col)
					if i!=mark:col=2 if col==1 else 1
			else:
				print(3)
				s=[1,2]*(n//2)+[3]

		else:
			print(2)
			s=[1,2]*(n//2)
		print(*s)




