def check(arr):24 36
    count=0
    for i in arr:
        if i%4==0 and i%6==0:
            print(i,end=' ')
            count+=1
    return count
arr=list(map(int,input().split()))
print('the count is:',check(arr))
