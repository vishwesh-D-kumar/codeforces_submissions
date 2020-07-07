k=int(input())
x=10
y=0

while(y!=k):
	# print(x)
	s=0
	for i in str(x):
		s+=int(i)
		if s>10:
			break
	if s==10:
		y+=1
		# print(x)
		if y!=k:
			x+=9
	else:
		x+=9
print(x)
