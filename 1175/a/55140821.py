t=int(input())
for baka in range(t):
	n,k=list(map(int,input().split()))
	c=0
	while(n!=0) :
		l=n%k
		# print(n)
		# print(l,n,c)
		# n-=l
		# n/=k
		# c+=l
		# if n!=0;
		# print(c,n)
		if l:
			n-=l
			c+=l

		else:
			n=(n//k)
			c+=1
			
			

	print(int(c))