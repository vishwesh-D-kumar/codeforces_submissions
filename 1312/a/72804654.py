def I():return list(map(int,input().split()))
for __ in range(int(input())):
	n,m=I()
	print("NO") if n%m else print("YES")
