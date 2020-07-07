y=int(input())
x=0
for i in range(y):
    oper=input()
    if '++' in oper:
        x+=1
    if "--" in oper:
        x-=1
print(x)
        