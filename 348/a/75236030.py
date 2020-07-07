import math
def I(): return(list(map(int,input().split())))
n=int(input())
a=I()
sa=sum(a)
ans=max(max(a),math.ceil(sa/(n-1)))
print(ans)