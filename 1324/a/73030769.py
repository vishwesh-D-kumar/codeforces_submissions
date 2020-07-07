def I():return list(map(int,input().split()))
for __ in range(int(input())):
	n=input()
	x=I()
	odd=0
	even=0
	for i in x:
		if i%2:odd=1 
		else :even=1
	print("NO") if (odd and even) else print("YES")