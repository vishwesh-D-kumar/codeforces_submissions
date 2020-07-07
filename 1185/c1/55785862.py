n,m=list(map(int,input().split()))
if n==1:
	print(0)
	exit(0)
t=list(map(int,input().split()))
x=[]
for i in range(len(t)):
	# j=0
	# s=0
	# br=0
	# while(j<len(x) and x[j]<=t[i]):
	# 	s+=x[j]
	# 	if s>m:
	# 		br=j
	# 	j+=1
	# x.insert(0,t[i])
	
	# if s<=m-t[i]:
	# 	if j==len(x)-1:
	# 		print(0)
	# 	else:
	# 		while(j<len(t)):
	# 			s+=x[j]
	# 			if s>m:
	# 				br=j
	# 				break
	# 		print(br)
	# else:
	# 	print(br)
	br=0
	s=0
	for j in range(len(x)):
		s+=x[j]
		br=j
		if s>m-t[i]:
			break
	if s<=m-t[i]:
		print(0,end=" ")
	else:
		print(len(x)-br,end=" ")
	x.append(t[i])
	x.sort()












