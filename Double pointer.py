# Double pointer
#two pointers
#first and last
#first increment and last is decrement


arr=[1,2,3,4,5,6]
k=6
count=0
f=0          #f=first
l=len(arr)-1 #l=last
while f<l:
    if arr[f]+arr[l]==k:
        count+=1
        f+=1
        l-=1
    elif arr[f]+arr[l]<k:
        f+=1
    else:
        l-=1
print(count)


