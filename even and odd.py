n=2397
m=3
''' output:592721
if even digit then add with m
if odd digit then multiply with m'''
n=str(n)
for i in n:
    if int(i)%2==0:
        print(int(i)+m,end='')
    else:
        print(int(i)*m,end='')
            
