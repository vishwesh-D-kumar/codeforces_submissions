for baka in range(int(input())):
	n,s,t=list(map(int,input().split()))
	if n==s and n==t:
		print(1)
		continue
	if s+t<=n:
		print(max(s,t)+1)
	else:
		print(max(s,t)-(s+t-n)+1)



