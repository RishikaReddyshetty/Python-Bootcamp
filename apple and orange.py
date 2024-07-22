s=7
t=11
a=3
b=15
apples=[6,5,-4]
oranges=[9,8,-4]
acount,ocount=0,0
for i in apples:
    if a+i in range(s,t+1):
        acount+=1
for i in oranges:
    if b+i in range(s,t+1):
        ocount+=1
print(acount,ocount)
