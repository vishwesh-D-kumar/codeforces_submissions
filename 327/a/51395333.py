def I():
	return((list(map(int,input().split()))))
n=int(input())
l=I()
su=[]
s=0

for i in l:
	s+=i
	su.append(s)
# print(su)
su.append(0)
m=s
a,b=0,0
for j in range (n):
	for i in range (j,n):
		mh=su[i]-su[j-1]
		# print(mh,i,j)
		if s-mh+(abs(i-j)-mh+1)>s-m+(abs(b-a)-m+1):

			m=mh
			a,b=i,j
		# elif mh==m and a-b<i-j:
		# 	a,b=i,j
		# print(i,j,mh)

print(s-m+(abs(b-a)-m+1))