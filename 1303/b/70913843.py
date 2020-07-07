def I(): return(list(map(int,input().split())))
import math
for t in range(int(input())):
	n,g,b=I()
	x=n
	n=math.ceil(n/2)
	numTimes=(g+b)*(n//g)
	if n%g==0:
		s=numTimes-b
	else:
		s=numTimes+(n%g)
	# badTiles=(s//(g+b))*(g+b)
	# if badTiles+s<x:
	# 	s+=(x-(badTiles+s))
	if s<x:
		s=x
	print(s)
