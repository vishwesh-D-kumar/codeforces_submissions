def I(): return(list(map(int,input().split())))


for __ in range(int(input())):
	s=input()
	finalstr=""
	n=len(s)
	f=0
	for i in range(n):
		if not s[i] in finalstr:
			if i!=0:	
				idx=finalstr.find(s[i-1])
				if idx==0:
					finalstr=s[i]+finalstr
				elif idx==len(finalstr)-1:
					finalstr+=s[i]
				else:
					f=1
					break
			else:
				finalstr+=s[i]
		else:
			idx1=finalstr.find(s[i])
			idx2=finalstr.find(s[i-1])
			if abs(idx1-idx2)>1:
				f=1
				break




	if f==1:
		print("NO")
	else:
		print("YES")
		for i in range(26):
			if chr(97+i) not in finalstr:
				finalstr+=chr(97+i)
		print(finalstr)
		


			# if idx!=len(finalarr)-1 or idx!=0:
			# 	if i!=n-1:

			# 		if s[i+1]!=finalarr[idx+1] and s[i+1]!=finalarr[idx-1]:
			# 			f=1
			# 			break
			# 	if i!=0:

			# 		if s[i-1]!=finalarr[idx+1] and s[i-1]!=finalarr[idx-1]:
			# 			f=1
			# 			break
			# if idx==len(finalarr)-1 and 





			# Check 




