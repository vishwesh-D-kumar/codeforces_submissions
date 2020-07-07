def I(): return(list(map(int,input().split())))
n,m=I()
for i in range(m):
	input()
s=""
for i in range(n):s+="1" if i%2 else "0"
print(s)