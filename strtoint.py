s=input()
sum=0
for i in range(0,len(s)):
    if s[i].isdigit():
        sum+=int(s[i])
print(sum)
