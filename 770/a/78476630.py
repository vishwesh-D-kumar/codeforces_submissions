def I(): return(list(map(int,input().split())))

n,k=I()
s2="".join([chr(i) for i in range(99,99+k-2)])
s1="ab"*((n-k+2)//2)
if (n-k+2)%2!=0:
	s1+="a"
# if k==2:
# 	print(s1) if len(s1)==n else print(s1+"a")
# else:
# 	print(s1+s2)
print(s2+s1)