def I():return list(map(int,input().split()))

for __ in range(int(input())):
	a,b=I()
	if a%b==0:print(0)
	else:print(b-a%b)