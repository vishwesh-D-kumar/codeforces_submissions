import sys
# input = sys.stdin.buffer.readline
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a

for __ in range(int(input())):
	n,k=I()
	s=input()
	onethere=False
	if "1" in s:
		onethere=True
	if n<=k+1:
		if not onethere:
			print(1)
			continue
		else:
			print(0)
			continue
	
	# i=-1 if s[0]=="0" else 0
	if not onethere:
		print((n-1)//(k+1)+1)
		continue
	ans=0
	ones=[]
	for i in range(n):
		if s[i]=="1":
			ones.append(i)
	if ones[0]>0:
		ans+=max(0,(ones[0]-k-1)//(k+1)+1)
	for i in range(len(ones)-1):
		nex=ones[i+1]
		prev=ones[i]
		c=max(0,(nex-prev-2-2*k)//(k+1)+1)
		# print(c,"##")
		ans+=c
	if ones[-1]<n-1:
		ans+=max(0,(n-ones[-1]-k-2)//(k+1)+1)

	print(ans)	



