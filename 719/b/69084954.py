# def I(): return(list(map(int,input().split())))
def solve(arr):
	# print(arr)
	f=min(arr.count("b"),arr.count("r"))
	return len(arr)-f

n=int(input())
s=input()

accs0=[]
accs1=[]

for i in range(n):
	if i%2==1:
		if s[i]=='r':
			accs0.append(s[i])
		else:
			accs1.append(s[i])
	else:
		if s[i]!='r':
			accs0.append(s[i])
		else:
			accs1.append(s[i])
print(min(solve(accs1),solve(accs0)))
			





