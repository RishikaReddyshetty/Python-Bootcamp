#fibnocci series55
#n=8
#0 1 1 2 3 5 8 13
'''def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))'''# normal user have to give input n=8 ouput=21

#  starting index from 1
'''def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=5
print(fib(n-1))''' #output=3


# finding nth fibonacci series(starting index from 0)
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=5
print(fib(n))    #output=5
