def I(): return(list(map(int,input().split())))

for __ in range(int(input())):
	n,x=I()
	l=I()
	minHops=1000000000000000000000000000
	for a in l:
		x2=x
		if x2%a==0:
			minHops=min(x2//a,minHops)
		else:
			minHops=min((max(1,(x2//a))+1),minHops)
	print(minHops)




