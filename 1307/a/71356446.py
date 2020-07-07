def I(): return(list(map(int,input().split())))

for __ in range(int(input())):
	n,d=I()
	a=I()
	s=a[0]
	for i in range(1,n):
		if d>i*a[i]:
			s+=a[i]
			d-=(i*a[i])
		else:
			s+=d//i
			break
	print(s)





