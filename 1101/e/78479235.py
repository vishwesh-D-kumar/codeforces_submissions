def I(): return(list(map(int,input().split())))
maxx=0
maxy=0
r=""
for __ in range(int(input())):
	s=input().split()
	x,y=min([int(s[1]),int(s[2])]),max(int(s[1]),int(s[2]))
	if s[0]=="+":
		maxx=max(maxx,x)
		maxy=max(maxy,y)
	else:
		h,w=x,y
		# print(maxy,maxx)
		if h<maxx or w<maxy:
			r+="NO\n"
		else:
			r+="YES\n"
print(r)