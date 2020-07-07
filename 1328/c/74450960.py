def I():return list(map(int,input().split()))

for __ in range(int(input())):
	a=""
	b=""
	n=int(input())
	c=input()
	f=False
	for i in range(n):
		if c[i]=="1":
			if f:
				a+="1"
				b+="0"
				
			else:
				a+="0"
				b+="1"
				f=1
		elif c[i]=="0":
			a+="0"
			b+="0"
		else:
			if not f:
				a+="1"
				b+="1"
			else:
				a+="2"
				b+="0"
	print(a)	
	print(b)
	