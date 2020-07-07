str=input()
ans=''
str=str.lower()
for i in str:
    
    if i not in ['a','e','i','o','u','y'] :
        ans=ans+'.'+i
print(ans)