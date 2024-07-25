n1=7826
n2=5489
n3=1386
'''
sum of all min digit
sum of all max digit
and find the difference'''

#find the min and max numbers
'''
def check(n):
    s=str(n)
    min=int(s[0]) #type casting
    max=int(s[0]) #type casting
    for i in s:
        if int(i)<min:
            min=int(i)
        if int(i)>max:
            max=int(i)
    print(min,max)
check(n1)
check(n2)
check(n3)
'''

            

 
#find the differences of min and max
n1=6521
n2=9078
n3=2486
max_sum=0
min_sum=0
def min_check(n):
    s=str(n)
    min=int(s[0]) #type casting
    for i in s:
        if int(i)<min:
            min=int(i)
    return min
def max_check(n):
    s=str(n)
    max=int(s[0]) #type casting
    for i in s:
        if int(i)>max:
            max=int(i)
    return max
min_sum=min_check(n1)+min_check(n2)+min_check(n3)
max_sum=max_check(n1)+max_check(n2)+max_check(n3)
diff=abs(min_sum-max_sum)
print(diff)




            

 
