s=input().split()
n,k=int(s[0]),int(s[1])
if k==1:
    print(n)
else:
    print(pow(2,(len(bin(n)[2:])))-1)