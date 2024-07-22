'''Password validation
len >8
1 cap
1 small
1 digit
1 special char
s='Excellence@123
def check(s):
    up_c,low_c,sp_c,dig_c=0,0,0,0
    if len(s)>8:
        for i in range(len(s)):
            if s[i].isdigit():
                dig_c+=1
            elif s[i].isupper():
                up_c+=1
            elif s[i].islower():
                low_c+=1
            elif s[i].isascii():
                sp_c+=1
            else:
                break
        if dig_c>0 and up_c>0 and low_c>0 and sp_c>0:
             print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
string=input()
check(string)'''





s=input()
ucount,lcount,dcount,scount=0,0,0,0
for c in s:
    if c.isupper():
        ucount+=1
    elif c.islower():
        lcount+=1
    elif c.isdigit():
        dcount+=1

    else:
        scount+=1
if len(s)>0 and ucount>0 and lcount>0 and dcount>0 and scount>0:
    print('Valid')
else:
    print('Invalid')
