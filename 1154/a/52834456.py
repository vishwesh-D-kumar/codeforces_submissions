def I():
	return(list(map(int,input().split())))

# input()
x=I()
# sum=(x[0]+x[1]+x[2])/2
sum=max(x)
index=0
for i in range(len(x)):
	if x[i]==sum:
		index=i
x.pop(index)
# print(x)


print(int(sum-x[0]),int(sum-x[1]),int(sum-x[2]))
# a=x[0]+x[1]-x[3]
# b=x[0]-a
# c=x[0]-a
# print(a,b,c)