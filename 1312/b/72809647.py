def I():return list(map(int,input().split()))
for __ in range(int(input())):
	n=int(input())
	x=I()
	x.sort(reverse=True)
	print(*x)
