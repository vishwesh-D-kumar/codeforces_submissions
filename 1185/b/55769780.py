n=int(input())
for baka in range(n):
	a=input()
	b=input()
	i=0
	j=0
	c1=0
	c2=0
	while(i<len(a) and j<len(b)):
		if c1<c2:
			break

		if a[i]!=b[j]:
			break
		c1=0
		while(j<len(b) and a[i]==b[j]):
			c1+=1
			j+=1
		i+=1
		c2=1
		while(i<len(a) and a[i]==a[i-1]):
			c2+=1
			i+=1
		# print(c1,c2)
		if c1<c2:
			# print("yeah")
			break
	if i==len(a) and j==len(b) and c1>=c2:
		print("YES")
	else:
		print("NO")



