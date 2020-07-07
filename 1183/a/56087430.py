a=int(input())
s=0

for i in str(a):
	s+=int(i)
if s%4==0:
	print(a)
else:
	i=a
	while(s%4!=0):
		s=0
		for j in str(i):
			s+=int(j)
		i+=1
	print(i-1)
