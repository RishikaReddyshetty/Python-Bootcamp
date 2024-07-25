#print 0's then 1's
'''
arr=[1,1,0,1,1,0,0]
output:
    0,0,0,1,1,1,1'''


arr=[1,1,0,1,1,0,0]    
ones=[]
zeros=[]
for i in arr:
    if i==0:
        zeros.append(i)
    else:
        ones.append(i)
zeros.extend(ones)
print(zeros)
