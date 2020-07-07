def I():return list(map(int,input().split()))
for __ in range(int(input())):
 	# n=int(input())
 	s=input()
 	s+="R"
 	d=1
 	i=len(s)-1
 	
 	while(i>=0):
 		final=i
 		i-=1
 		while(i>=0 and s[i]!="R"):i-=1
 		d=max(d,final-i)
 	print(d)







 		

