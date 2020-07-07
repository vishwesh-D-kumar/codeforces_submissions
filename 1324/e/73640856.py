def I():return list(map(int,input().split()))


n,h,l,r=I()
a=I()
dp=[]
for i in range(n):
	dp.append([-1]*h)
# print(dp)
def rec(i,j):
	c=0
	if l<=j and j<=r and i!=0:
		c=1
	if i>n-1 :
		# print(i,j,"End")
		return c
	# print(i,j)
	if dp[i][j]!=-1:return dp[i][j]
	else:

		# print(c)
		s=max(rec(i+1,(j+a[i]-1)%h),rec(i+1,(j+a[i])%h))+c
		dp[i][j]=s
		return s
print(rec(0,0))
# print(dp)