# Sum of natural numbers
def sum_of_natural(n):
    if n==1:
        return 1
    else:
        return n+sum_of_natural(n-1)
print(sum_of_natural(5)) #output 1 2 3 4 5=sum15


