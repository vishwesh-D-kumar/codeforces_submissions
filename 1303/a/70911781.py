def I(): return(list(map(int,input().split())))
for t in range(int(input())):
	s=input()
	# print(s)
	c=0
	f=0
	i=0
	while(i<len(s)):
		if s[i]=="1":
			while(i<len(s) and s[i]=="1"):
				i+=1
				# continue
			if(i<len(s)):
				ct=0
				while(i<len(s) and s[i]=="0"):
					ct+=1
					i+=1
				if(i<len(s)):
					c+=ct
		else:
			i+=1
	print(c)

	# s.split("1")
