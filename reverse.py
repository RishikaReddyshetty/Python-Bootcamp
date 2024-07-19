#s='sridevi is engineering college'
#reverse the string
def check(s):
    rev=''
    for i in s:
        rev=i+rev
    print(type(rev))
    return rev
s='sridevi is engineering college'
print(check(s))
