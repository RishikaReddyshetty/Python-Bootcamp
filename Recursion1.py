#Recursion:
'''def fact(n):5
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))'''



# without recursion for loop
n=5
fact=1
for i in range(1,n+1):
    fact=fact*n
print(fact)
