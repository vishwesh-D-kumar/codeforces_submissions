def I(): return list(map(int,input().split()))
for i in range(int(input())):
	l=r,g,b=I()
	m=max(r,g,b)
	l.remove(m)
	if l[0]+l[1]<m-1:
		print("No")
	else:
		print("Yes")

