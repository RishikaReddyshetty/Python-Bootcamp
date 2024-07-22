#Good Numbers:
    #arr=[35,9,1]
    #res=low cube + high cube

'''
import math
arr=[35,9,1]
c=0
res=0
for i in arr:
    low=1
    high=math.floor(math.cbrt(i))
    while low<high:
        res=(low**3)+(high**3)
        if res!=i:
            low+=1
        else:
            c+=1
            break
print(c)
'''

#or same before code
import math
arr=[35,9,1,65,126,133]
count=0
for ele in arr:
    low=1
    high=math.ceil(ele**0.3)
    while low<high:
        res=low**3 + high**3
        if res==ele:
            count+=1
        low+=1
print('The count is:',count)
            
            
