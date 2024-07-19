#s='sridevi is engineering college'
#reverse the string
def check(s):
    s=s.split()
    s=list(reversed(s)) # s became reverse list
    print(s)
    for i in s:
        rev=i[::-1]# characters of reverse list
        print(rev,end=' ')
s='sridevi is engineering college'
check(s)
