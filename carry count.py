'''
   11
n1=288
n2=594
------
   882
'''

#count the number of carry
n1=2789
n2=5321
carry=0
count=0
while n1>0 and n2>0:
    rem1=n1%10 #2
    rem2=n2%10 #5
    sum=rem1+rem2+carry
    if(sum>9):
        carry=1
        count+=1
    else:
        carry=0
    n1=n2//10
    n2=n2//10
print(count)

