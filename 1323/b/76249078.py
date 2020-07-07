def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a




n,m,k=I()
a=I()
b=I()
newa=[]
newb=[]
i=0
da={}
db={}
while(i<n):
	while(i<n and a[i]==0):i+=1
	c=0
	j=i
	while(i<n and a[i]==1):
		i+=1
	for subl in range(1,i-j+1):
		if k%subl==0:
			da[subl]=da.get(subl,0)+(i-j+1-subl)


	newa.append(c)
newa.sort()

i=0
while(i<m):
	while(i<m and b[i]==0):i+=1
	c=0
	j=i
	while(i<m and b[i]==1):
		i+=1
		# c+=1
		# db[c]=db.get(c,0)+1
	for subl in range(1,i-j+1):
		db[subl]=db.get(subl,0)+(i-j+1-subl)

	newb.append(c)
newb.sort()
n=len(newb)
m=len(newb)
prefb=[0]*(m+1)

prefb[0]=newb[0]
for i in range(1,m):
	prefb[i]=prefb[i-1]+newb[i]
l=0
r=m-1
ans=0
# print(newa)
# print(newb)
# print(da)
# print(db)
for i in da.keys():
	ans+=da[i]*db.get(k//i,0)

# for i in range(n):
# 	if k%newa[i]==0:
# 		while(r>=0 and newb[r]>=newa[i]//k):r-=1
# 		ans+=(prefb[m]-prefb[r])-(min(m-r,m))*(k//newa[i]+1)
print(ans)



