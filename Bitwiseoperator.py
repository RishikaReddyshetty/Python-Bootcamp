s='1C0C1C1A0B1'   #bitwise operator
res=int(s[0])
for i in range(1,len(s),2):
    if s[i]=='A':
        res=res&int(s[i+1]) #AND 
    elif s[i]=='B':
        res=res|int(s[i+1])  #OR
    elif s[i]=='C':
        res=res^int(s[i+1])  #XOR
print(res)  #output 1


'''s='1A1B1C0C1B0A1'   #bitwise operator 
res=int(s[0])
for i in range(1,len(s),2):
    if s[i]=='A':
        res=res&int(s[i+1])
    elif s[i]=='B':
        res=res|int(s[i+1])
    elif s[i]=='C':
        res=res^int(s[i+1])
print(res) '''  #output 0







'''FOR
IF     I=='A'      &
ELIF   I=='B'      |
ELSE   I=='C'      ^'''
