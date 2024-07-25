'''
s='{[()]}'
#if stack is empty then it is balanced
#if stack is not empty then it is unbalance
open_brackets=['(','[','{']
stack=[]
for i in s:
    if i in open_brackets:
        stack.append(i)
    else:
        if i==')' and stack[-1]=='(':
            stack.pop()
        elif i=='}' and stack[-1]=='{':
            stack.pop()
        elif i==']' and stack[-1]=='[':
            stack.pop()
        else:
            continue
if stack==[]:
    print("Balanced")
else:
    print("Unbalanced")'''


def check(s):
    stack=[]
    openings=['(','[','{']
    brackets={'(':')','[':']','{':'}'}
    for i in s:
        if i in openings:
            stack.append(i)
        else:
            if stack:
                top=stack.pop()
                if brackets[top]!=i:
                    return 'NO'
            else:
                return 'NO'
    if stack:
        return 'No'
    else:
        return 'Yes'
s='}{}'
print(check(s))
