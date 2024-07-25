# convert binary number to decimal number
'''
n=101011
1*2**0=1
1*2**1=2
0*2**2=0
1*2**3=8
0*2**4=0
1*2**5=32
1+2+0+8+0+32=43
'''

n=101011
sum=0
i=0
while n>0:
    rem=n%10
    pro=rem*pow(2,i)
    sum+=pro
    i+=1
    n=n//10
print(sum)

