def I():
	return(sorted(list(map(int,input().split()))))
n=I()[0]

b=I()

m=I()[0]

g=I()

i,j,k=[0]*3

while i<n and j<m:

	if abs(b[i]-g[j])<2:k+=1;i+=1;j+=1

	elif b[i]<g[j]:i+=1

	else:j+=1

print(k)