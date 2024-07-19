n=int(input())
pro=1
while n>0:
    rem=n%10
    pro=pro*rem
    n=n//10
print('The product is:',pro)    
