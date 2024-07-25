#check whether the two strings are anagram
s1='swec'
s2='cesw'
res1=sorted(s1)
res2=sorted(s2)
if len(s1)==len(s2) and res1==res2:
    print('Anagram')
else:
    print('Not')
