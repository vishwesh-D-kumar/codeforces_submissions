def x(n):
	if n==1:
		return(1)
	else:
		return x(n-1)+4*(n-1)
print(x(int(input())))