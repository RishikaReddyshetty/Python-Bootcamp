#arr=[1,36,24,9,2,12]
#count how many number are divisble of 4 & 6
#pass this arr as function parameter
def check(arr):
    count=0
    for i in arr:
        if i%4==0 and i%6==0:
            print(i,end=' ')
            count+=1
    return count
arr=[1,36,9,24,4,2,12]
print('The count is:',check(arr))
