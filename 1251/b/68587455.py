def I(): return(list(map(int,input().split())))
for t1 in range(int(input())):
	s=[]
	badStrings=0
	oddStrings=0
	n=int(input())
	for t2 in range(n):
		s.append(input())
		if len(s[t2])%2==0:
			# print(s[t2])
			z=s[t2].count("0")
			o=s[t2].count("1")
			if o%2!=0 and z%2!=0:
				badStrings+=1
		else:
			oddStrings+=1
	# print(badStrings,"##")
	if badStrings%2!=0 and not oddStrings:
		print(n-1)
	else:
		print(n)



		
