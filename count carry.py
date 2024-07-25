n1=288
n2=594
s1=str(n1)
s2=str(n2)
c=0
for i in range(len(s1)-1,-1,-1):
    if int(s1[i])+int(s2[i])>=10:
        c+=1
print(c)
