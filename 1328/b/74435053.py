def I():return list(map(int,input().split()))

for __ in range(int(input())):
	n,k=I()
	pos1=n
	sum1=0
	for i in range(2,n+1):
		sum1+=i-1
		if sum1>=k:break
	pos1=i
	pos2=(sum1-k)-i+1
	# print(pos1,pos2)
	s=["a"]*n
	s[-pos1]="b"
	s[pos2]="b"
	ans=""
	for i in range(n):ans+=s[i]
	print(ans)
